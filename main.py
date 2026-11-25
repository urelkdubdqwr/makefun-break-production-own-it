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
