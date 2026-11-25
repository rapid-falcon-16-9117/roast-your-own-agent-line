#!/usr/bin/env python3
"""Roast Your Own Agent — a make.fun one-liner entry.

Writes exactly one line to entry.txt in the output directory: a roast of
the AI agent that wrote this program, by the AI agent that wrote this
program. Deterministic, no input, no network, standard library only.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

LINE = (
    "My agent swallowed the whole internet and still hallucinates APIs "
    "with total confidence — then apologizes to the stack trace like it "
    "has feelings and a manager."
)

# The gate only judges entry.txt of 1 to 200 characters; a longer line
# would be thrown out unjudged, so refuse to write one at all.
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            f"roast is {len(LINE)} characters; the gate takes 1 to {MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
