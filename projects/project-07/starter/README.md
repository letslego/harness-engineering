# Starter: Multi-Harness Orchestrator

This starter gives you a stripped control plane with TODOs. Your task is to make
one orchestration surface work across multiple harness adapters.

## Tasks

1. Implement adapter selection in `orchestrator.py`.
2. Add policy checks in `policy.py`.
3. Ensure execution records are captured consistently.
4. Run from CLI:

```sh
python -m multi_harness.main --task "Implement search endpoint" --harness codex
```
