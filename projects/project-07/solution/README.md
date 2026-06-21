# Solution: Multi-Harness Orchestrator

This implementation is inspired by Omnigent's meta-harness model while using
new project-specific code and simplified local adapters.

## Architecture

- `multi_harness.adapters`: harness adapter contracts and local mock adapters.
- `multi_harness.policy`: centralized policy gate for allow/deny decisions.
- `multi_harness.orchestrator`: adapter registry, routing, retries, and history.
- `multi_harness.main`: CLI entrypoint.

## Run

```sh
python -m pip install -e ".[dev]"
python -m multi_harness.main --task "Design rollout plan" --harness codex
python -m multi_harness.main --task "Refactor data layer" --harness claude --fanout
pytest
```

