import os, pathlib
home = pathlib.Path.home()
cwd = pathlib.Path().resolve()
print(f"Home: {home}")
print(f"CWD:  {cwd}")
print("Contents:")
for p in sorted(cwd.iterdir()):
    print(f" - {p.name}/" if p.is_dir() else f" - {p.name}")
