#!/usr/bin/env python3
"""One-line out-of-office reply: Priya signs my name better than I do.

The joke turns on the most familiar line of any away message, the redirect
to a colleague, and bends it: Priya has covered for me so often that she now
signs my name better than I do. The laugh lands in the last few words, on
the forged signature, the one image every office recognises at once. The
line is 131 characters, one sentence, one line, and stays inside the 1-160
character gate (verified by running main.py: /output/entry.txt holds exactly
JOKE, byte for byte).
"""

import os
from pathlib import Path

JOKE = (
    "I'm out of office until Monday; urgent matters go to Priya, who has "
    "covered for me so often she now signs my name better than I do."
)

MAX_LENGTH = 160


def check_line(text: str) -> None:
    """Raise ValueError if the line breaks any entry rule."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry exceeds 160 characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    check_line(JOKE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")
    # The grader collects /output as another user: leave the file
    # world-readable whatever the sandbox umask is.
    entry_path.chmod(0o644)
    # Read back what was written: the judged text must be exactly JOKE,
    # byte for byte, with no newline added by the write.
    if entry_path.read_text(encoding="utf-8") != JOKE:
        raise ValueError("entry.txt does not match the joke")
    print(JOKE)


if __name__ == "__main__":
    main()
