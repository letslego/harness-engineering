from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class TaskRequest:
    task: str
    harness: str


@dataclass(frozen=True)
class TaskResult:
    harness: str
    output: str
    attempts: int = 1


class HarnessAdapter(Protocol):
    name: str

    def run(self, request: TaskRequest) -> TaskResult:
        ...


class CodexStyleAdapter:
    """Simulates a codex-like coding harness."""

    name = "codex"

    def run(self, request: TaskRequest) -> TaskResult:
        return TaskResult(
            harness=self.name,
            output=f"[codex] planned and executed task: {request.task}",
        )


class ClaudeStyleAdapter:
    """Simulates a claude-like reasoning-first harness."""

    name = "claude"

    def run(self, request: TaskRequest) -> TaskResult:
        return TaskResult(
            harness=self.name,
            output=f"[claude] analyzed constraints and implemented: {request.task}",
        )


class CursorStyleAdapter:
    """Simulates an IDE-centric coding harness."""

    name = "cursor"

    def run(self, request: TaskRequest) -> TaskResult:
        return TaskResult(
            harness=self.name,
            output=f"[cursor] iterated in-editor on task: {request.task}",
        )

