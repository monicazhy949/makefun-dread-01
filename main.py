"""Two Days of Quiet Dread — revised entry.

Writes a single-line code review comment approving a PR with quiet
existential dread to /output/entry.txt.

Revision vs draft 1: dropped the plant / empty-house metaphor, which
read literary and a little melodramatic. The revised line keeps the
approval flat and first-person, and lets the dread come from the
reviewer himself — a future version of me already sighing at this
exact diff — which reads like something a tired engineer would
actually paste before clicking approve.
"""

import os

ENTRY = (
    "Approved. It works, the tests pass, and somewhere a future "
    "version of me is already sighing at this exact diff."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
