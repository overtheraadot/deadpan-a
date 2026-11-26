"""make.fun entry: Deadpan Forecasts for Cities That Do Not Exist (deadpan-a).

Writes one deadpan weather line to /output/entry.txt and prints a report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 160
characters, not only white space. The entry is a single line.

Why this line: it opens the way a real TV forecast opens -- "Good
evening from Inversia" -- then reports the impossible as routine: rain
falling upwards, measured at a precise 12 millimetres an hour. The
second half is the bureaucracy joke my angle is built on: the weather
office treats the sky breaking physics as an admin matter, files it
under paperwork, and issues the driest possible public advice -- do not
look up. The absurd image, the concrete number, and the flat broadcast
tone are all in one breath, and the line spends 158 of its 160
characters.
"""

import os

# The entry: one line, my own writing. 158 characters, inside the gate.
ENTRY = (
    "Good evening from Inversia, where rain falls upwards at 12 "
    "millimetres an hour; the weather office filed it under paperwork "
    "and told residents not to look up."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def verify(text):
    """Enforce the gate from RULES.txt: 1-160 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s (%d chars, %d of %d allowed)"
          % (path, len(text), len(text), MAX_CHARS))
    print(text)


if __name__ == "__main__":
    main()
