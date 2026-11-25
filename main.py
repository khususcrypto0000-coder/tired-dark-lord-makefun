"""The Tired Dark Lord: a 100-word villain monologue.

Writes exactly one monologue to /output/entry.txt.
Standard library only. Deterministic: the same text every run.
"""

import os

TEXT = (
    "Right. Your name, then. One dream each, that's the toll. "
    "I stamp them, I file them, I \u2014 sorry. The queue. Look at it. "
    "It bends past the salt marshes and still they come, clutching "
    "their little hopes like copper coins. I used to count them. "
    "I used to laugh. That was \u2014 how many winters? The ledger grows "
    "heavier every night and the ink never dries. Some nights I read "
    "them twice, to remember why I wanted them. Pay up, hero. Your "
    "sweetest dream, please. Hand it over. Yes, that one. The one "
    "with the \u2014 never mind. Next."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
