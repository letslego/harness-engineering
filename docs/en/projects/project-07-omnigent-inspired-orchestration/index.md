[中文版本 →](../../../zh/projects/)

> Related lecture: [Lecture 11. Make the agent's runtime observable](./../../lectures/lecture-11-why-observability-belongs-inside-the-harness/)  
> Template files: [templates/](https://letslego.github.io/harness-engineering/en/resources/templates)

# Project 07. Build an Omnigent-Inspired Meta-Harness

## What You Do

In this project, you build a meta-harness layer that can route the same task to
multiple coding harness adapters (Codex-style, Claude-style, Cursor-style) under
one shared policy and execution-history surface.

Reference inspiration: [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)

The goal is not to clone Omnigent internals. The goal is to implement the same
core pattern in a smaller project-specific design:

- one orchestrator entry point
- pluggable harness adapters
- shared policy gating
- deterministic execution records

## Use the Checked-In Project

Repository path: [`projects/project-07/`](https://github.com/letslego/harness-engineering/tree/main/projects/project-07)

| Directory | What it contains | What to compare |
|------|------|------|
| [`starter/`](https://github.com/letslego/harness-engineering/tree/main/projects/project-07/starter) | Interface skeleton with TODOs for adapter routing and policy enforcement. | Your completed orchestrator implementation. |
| [`solution/`](https://github.com/letslego/harness-engineering/tree/main/projects/project-07/solution) | Reference implementation with adapter registry, task fanout, policy gate, CLI entrypoint, and tests. | Compare your architecture and failure handling against the reference. |

## Suggested Task Sequence

1. Implement harness adapter dispatch from task requests.
2. Add policy checks to block unsafe tasks before execution.
3. Record consistent execution history (blocked/failed/passed).
4. Add fanout execution across multiple harnesses.
5. Validate with tests and CLI runs.

