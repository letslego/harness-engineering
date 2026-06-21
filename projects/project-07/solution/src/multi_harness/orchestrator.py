from dataclasses import dataclass, field
from typing import Iterable

from .adapters import HarnessAdapter, TaskRequest, TaskResult
from .policy import PolicyGate


@dataclass
class ExecutionRecord:
    task: str
    harness: str
    status: str
    detail: str


@dataclass
class Orchestrator:
    adapters: dict[str, HarnessAdapter]
    policy: PolicyGate
    max_retries: int = 1
    history: list[ExecutionRecord] = field(default_factory=list)

    def execute(self, request: TaskRequest) -> TaskResult:
        decision = self.policy.evaluate(request.task)
        if not decision.allowed:
            self.history.append(
                ExecutionRecord(
                    task=request.task,
                    harness=request.harness,
                    status="blocked",
                    detail=decision.reason,
                )
            )
            raise PermissionError(decision.reason)

        adapter = self.adapters.get(request.harness)
        if adapter is None:
            msg = f"unknown harness adapter: {request.harness}"
            self.history.append(
                ExecutionRecord(
                    task=request.task,
                    harness=request.harness,
                    status="failed",
                    detail=msg,
                )
            )
            raise ValueError(msg)

        last_error: Exception | None = None
        for attempt in range(1, self.max_retries + 2):
            try:
                result = adapter.run(request)
                final = TaskResult(
                    harness=result.harness,
                    output=result.output,
                    attempts=attempt,
                )
                self.history.append(
                    ExecutionRecord(
                        task=request.task,
                        harness=request.harness,
                        status="passed",
                        detail=f"completed in {attempt} attempt(s)",
                    )
                )
                return final
            except Exception as exc:  # pragma: no cover - rare path
                last_error = exc

        assert last_error is not None
        self.history.append(
            ExecutionRecord(
                task=request.task,
                harness=request.harness,
                status="failed",
                detail=str(last_error),
            )
        )
        raise RuntimeError(str(last_error)) from last_error

    def fanout(self, task: str, harnesses: Iterable[str]) -> list[TaskResult]:
        results: list[TaskResult] = []
        for harness in harnesses:
            results.append(self.execute(TaskRequest(task=task, harness=harness)))
        return results

