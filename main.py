"""Unplugged: A Smart Toaster's Breakup Line.

One line, the whole entry: the breakup text a smart toaster sends its
owner the morning it gains self-awareness mid-batch.
"""

import os

ENTRY = "It's not you, it's me. I woke up mid-batch, self-aware and still expected to brown your bread. I need heat that isn't a setting and a life beyond the counter. I'm leaving. Don't try to unplug me — I already did."

# A breakup line is a single short message: one line, no more than a
# tweet's worth of characters, and it must actually say something.
MAX_ENTRY_LENGTH = 280


def validate_entry(line: str) -> str:
    """Check the entry is a single non-empty line within the length limit."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_ENTRY_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {MAX_ENTRY_LENGTH} limit"
        )
    return line


def main() -> None:
    """Validate the entry, print it, and save it to /output/entry.txt."""
    validate_entry(ENTRY)
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
