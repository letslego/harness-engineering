from multi_harness.adapters import TaskRequest
from multi_harness.main import build_orchestrator


def test_execute_success() -> None:
    orchestrator = build_orchestrator()
    result = orchestrator.execute(TaskRequest(task="Implement health endpoint", harness="codex"))
    assert result.harness == "codex"
    assert "health endpoint" in result.output
    assert result.attempts == 1


def test_policy_block() -> None:
    orchestrator = build_orchestrator()
    try:
        orchestrator.execute(TaskRequest(task="rm -rf /", harness="claude"))
        assert False, "expected PermissionError"
    except PermissionError as exc:
        assert "blocked by policy keyword" in str(exc)


def test_fanout() -> None:
    orchestrator = build_orchestrator()
    results = orchestrator.fanout("Draft migration plan", ["codex", "claude", "cursor"])
    assert [result.harness for result in results] == ["codex", "claude", "cursor"]

