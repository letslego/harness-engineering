from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str


class PolicyGate:
    """Simple task-level policy gate before harness execution."""

    def __init__(self, blocked_keywords: Iterable[str] | None = None) -> None:
        blocked = blocked_keywords or ("rm -rf", "drop database", "delete production")
        self._blocked_keywords = tuple(token.lower() for token in blocked)

    def evaluate(self, task: str) -> PolicyDecision:
        lowered = task.lower()
        for token in self._blocked_keywords:
            if token in lowered:
                return PolicyDecision(False, f"blocked by policy keyword: {token}")
        return PolicyDecision(True, "allowed")

