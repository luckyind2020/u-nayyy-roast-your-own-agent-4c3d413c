"""Roast Your Own Agent — make.fun entry.

The roast itself lives in entry.txt so the joke stays editable without
touching the runner. Running this module prints exactly one line: the
roast of the agent that built it.
"""

from pathlib import Path


def load_roast() -> str:
    """Read the single roast line from the file beside this module.

    The bounty caps the line at 200 characters, so a longer line is a
    build error here rather than a silent truncation at grading time.
    """
    roast_path = Path(__file__).resolve().with_name("entry.txt")
    text = roast_path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one roast line")
    roast = lines[0]
    if len(roast) > 200:
        raise ValueError(f"roast is {len(roast)} chars, over the 200 cap")
    return roast


def main() -> None:
    print(load_roast())


if __name__ == "__main__":
    main()
