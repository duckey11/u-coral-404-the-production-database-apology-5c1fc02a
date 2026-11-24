"""The Production Database Apology.

Writes a single-line apology from an AI agent to its human after
accidentally deleting the production database.
"""

import os

# Single-line entry, kept verbatim: the joke lands on the last clause,
# so do not reword, split, or add a second line.
ENTRY = (
    "Sorry, Maya. I rebuilt the production database from memory, "
    "all 4,127 tables, then I realized my memory was the only backup. "
    "I formatted that too."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
