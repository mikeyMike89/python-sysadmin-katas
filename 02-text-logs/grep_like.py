import sys, pathlib
def main():
    if len(sys.argv) < 3:
        print("Usage: python grep_like.py <root_folder> <needle>")
        sys.exit(1)
    root = pathlib.Path(sys.argv[1]).expanduser().resolve()
    needle = sys.argv[2].lower()
    for path in root.rglob("*"):
        if path.is_file():
            try:
                text = path.read_text(errors="ignore")
            except Exception:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if needle in line.lower():
                    print(f"{path}:{i}: {line.strip()}")
if __name__ == "__main__":
    main()
