from dataclasses import dataclass


@dataclass
class PolicyDecision:
    allowed: bool
    reason: str


class PolicyGate:
    def evaluate(self, task: str) -> PolicyDecision:
        # TODO: add real checks (blocked commands, risky keywords, etc.)
        return PolicyDecision(allowed=True, reason="not implemented")

