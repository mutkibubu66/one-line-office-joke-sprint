#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life (at most 200 characters)
to /output/entry.txt. Pure standard library; no network, no secrets.
"""

import os

JOKE = "The fastest reply in our office is 'per my last email,' sent by someone who never read your first one."

def main() -> None:
    # Gate: the entry must be one non-empty line of 1-200 characters.
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 200, f"joke must be 1-200 chars, got {len(joke)}"
    assert "\n" not in joke, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
