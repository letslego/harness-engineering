from dataclasses import dataclass
from typing import Protocol


@dataclass
class TaskRequest:
    task: str
    harness: str


@dataclass
class TaskResult:
    harness: str
    output: str


class HarnessAdapter(Protocol):
    name: str

    def run(self, request: TaskRequest) -> TaskResult:
        ...


class CodexAdapter:
    name = "codex"

    def run(self, request: TaskRequest) -> TaskResult:
        return TaskResult(harness=self.name, output=f"[TODO] Codex handled: {request.task}")


class ClaudeAdapter:
    name = "claude"

    def run(self, request: TaskRequest) -> TaskResult:
        return TaskResult(harness=self.name, output=f"[TODO] Claude handled: {request.task}")

