import argparse

from .adapters import ClaudeStyleAdapter, CodexStyleAdapter, CursorStyleAdapter, TaskRequest
from .orchestrator import Orchestrator
from .policy import PolicyGate


def build_orchestrator() -> Orchestrator:
    return Orchestrator(
        adapters={
            "codex": CodexStyleAdapter(),
            "claude": ClaudeStyleAdapter(),
            "cursor": CursorStyleAdapter(),
        },
        policy=PolicyGate(),
        max_retries=1,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a multi-harness orchestrator task")
    parser.add_argument("--task", required=True)
    parser.add_argument("--harness", default="codex", choices=["codex", "claude", "cursor"])
    parser.add_argument(
        "--fanout",
        action="store_true",
        help="Run the same task against all available harnesses",
    )
    args = parser.parse_args()

    orchestrator = build_orchestrator()
    if args.fanout:
        results = orchestrator.fanout(args.task, ["codex", "claude", "cursor"])
        for result in results:
            print(f"{result.harness}: {result.output} (attempts={result.attempts})")
        return

    result = orchestrator.execute(TaskRequest(task=args.task, harness=args.harness))
    print(f"{result.harness}: {result.output} (attempts={result.attempts})")


if __name__ == "__main__":
    main()

