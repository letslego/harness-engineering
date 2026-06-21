# Project 07: Omnigent-Inspired Multi-Harness Orchestration

This project introduces a meta-harness pattern inspired by [Omnigent](https://github.com/omnigent-ai/omnigent): one control
plane coordinating multiple coding harness adapters with shared policy checks and
consistent execution logs.

## Directory Guide

| Directory | Meaning |
|------|------|
| `starter/` | Learning scaffold with interfaces and TODOs to implement adapter routing, policy checks, and orchestration loops. |
| `solution/` | Reference implementation with a runnable CLI, policy gates, adapter abstraction, and tests. |

## Learning Goals

- Build a harness-neutral adapter interface.
- Route one task across multiple harnesses with shared contracts.
- Enforce allow/deny policy checks before adapter execution.
- Keep deterministic, inspectable execution records for each run.

## How to Use

```sh
cd starter
python -m pip install -e .
python -m multi_harness.main --task "Create release checklist" --harness codex

cd ../solution
python -m pip install -e .
python -m multi_harness.main --task "Draft CI migration plan" --harness claude
python -m pytest
```

