import argparse
import sys

from .ai import get_ai_response


def interactive_shell(model: str) -> int:
    """Start an interactive AI shell."""
    print("tshell AI shell. Type 'exit' to quit.")
    while True:
        try:
            prompt = input('> ')
        except EOFError:
            break
        if prompt.strip().lower() in {'exit', 'quit'}:
            break
        response = get_ai_response(prompt, model=model)
        print(response)
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="tshell: simple AI shell tool")
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Command to send to the AI (leave empty for interactive mode)",
    )
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo",
        help="OpenAI model to use (default: gpt-3.5-turbo)",
    )
    args = parser.parse_args(argv)

    if args.command:
        prompt = " ".join(args.command)
        print(get_ai_response(prompt, model=args.model))
        return 0

    return interactive_shell(args.model)


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
