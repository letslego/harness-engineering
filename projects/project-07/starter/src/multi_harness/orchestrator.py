from dataclasses import dataclass, field

from .adapters import HarnessAdapter, TaskRequest, TaskResult
from .policy import PolicyGate


@dataclass
class Orchestrator:
    adapters: dict[str, HarnessAdapter]
    policy: PolicyGate
    history: list[TaskResult] = field(default_factory=list)

    def execute(self, request: TaskRequest) -> TaskResult:
        decision = self.policy.evaluate(request.task)
        if not decision.allowed:
            raise PermissionError(decision.reason)

        # TODO: resolve adapter from request.harness and run it.
        raise NotImplementedError("Implement adapter dispatch and history recording")

