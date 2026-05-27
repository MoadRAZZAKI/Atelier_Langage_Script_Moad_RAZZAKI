from pathlib import Path

def decomposer(chemin: str) -> tuple[str, str, str]:
    p = Path(chemin)
    return str(p.parent), p.stem, p.suffix

exemples = [
    "/tmp/exemple.txt",
    "/var/log/archive.tar.gz",
    "/etc/hosts",
]

for chemin in exemples:
    print(f"{chemin:<30} -> {decomposer(chemin)}")