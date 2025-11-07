import sys, pathlib, datetime
def main():
    if len(sys.argv) < 3:
        print("Usage: python bulk_rename_prefix.py <folder> <prefix>")
        sys.exit(1)
    folder = pathlib.Path(sys.argv[1]).expanduser().resolve()
    prefix = sys.argv[2]
    if not folder.is_dir():
        print(f"Not a directory: {folder}")
        sys.exit(2)
    count = 0
    for f in folder.iterdir():
        if f.is_file():
            new = f.with_name(f"{prefix}{f.name}")
            f.rename(new)
            count += 1
    print(f"Renamed {count} files in {folder}")
if __name__ == "__main__":
    main()
