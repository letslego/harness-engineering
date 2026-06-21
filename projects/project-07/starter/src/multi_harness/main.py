import argparse

from .adapters import ClaudeAdapter, CodexAdapter, TaskRequest
from .orchestrator import Orchestrator
from .policy import PolicyGate


def main() -> None:
    parser = argparse.ArgumentParser(description="Starter multi-harness runner")
    parser.add_argument("--task", required=True)
    parser.add_argument("--harness", default="codex", choices=["codex", "claude"])
    args = parser.parse_args()

    orchestrator = Orchestrator(
        adapters={"codex": CodexAdapter(), "claude": ClaudeAdapter()},
        policy=PolicyGate(),
    )
    result = orchestrator.execute(TaskRequest(task=args.task, harness=args.harness))
    print(result.output)


if __name__ == "__main__":
    main()

