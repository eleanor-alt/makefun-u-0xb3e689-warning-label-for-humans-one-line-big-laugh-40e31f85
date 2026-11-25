#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt, as required by the competition gate (UTF-8 text,
1 to 160 characters, not only white space).

The label imitates a real printed warning label, and the laugh lands
in the last few words: the human reads the warning, nods wisely --
and then does the exact thing it forbids. That is how humans actually
behave around warning labels.
"""

import os

LABEL = (
    "WARNING: This human will read this label, nod wisely, "
    "and then do the exact thing it forbids."
)

OUTPUT_PATH = "/output/entry.txt"

# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 160 characters, not only white space. A single line, since
# the entry is one line of comedy.
MAX_CHARS = 160


def validate(label: str) -> None:
    """Refuse to write a label that would fail the competition gate."""
    if not label.strip():
        raise ValueError("label must not be only white space")
    if len(label) > MAX_CHARS:
        raise ValueError(
            f"label is {len(label)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in label or "\r" in label:
        raise ValueError("label must be a single line")


def main() -> None:
    validate(LABEL)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LABEL)
    # Read back and re-check what was actually written.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == LABEL, "written output differs from the label"
    print(f"Wrote {len(LABEL)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
