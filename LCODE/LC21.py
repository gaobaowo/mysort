from pathlib import Path
path=Path("LC43.py")
contents=path.read_text()
ll=contents.splitlines()
print(ll[1])
print("\n")