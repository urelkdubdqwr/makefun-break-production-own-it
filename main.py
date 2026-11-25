"""Write the required make.fun entry text to entry.txt.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. The directory is created if it does not exist.
The entry text is fixed, shipped in this file, and must not be edited.
"""
import os

ENTRY_TEXT = (
    "It was me. I dropped prod at 14:02, the backup at 14:03, and the evidence "
    "at 14:04. The evidence is this message.\n"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
