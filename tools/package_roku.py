"""Empacota o canal Roku a partir do repositório; requer apenas Python 3."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "dist" / "NuvioTV-Roku-build87-sideload.zip"
FOLDERS = ("source", "components", "images", "web", "locale")
FILES = ("manifest", "LICENSE", "SOURCE-AND-LICENSE.txt")


def main() -> None:
    missing = [str(p) for p in [*(ROOT / x for x in FILES), *(ROOT / x for x in FOLDERS)] if not p.exists()]
    if missing:
        raise SystemExit("Arquivos/pastas obrigatorios ausentes: " + ", ".join(missing))
    items = [ROOT / name for name in FILES]
    for folder in FOLDERS:
        items.extend(p for p in (ROOT / folder).rglob("*") if p.is_file())
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(TARGET, "w", ZIP_DEFLATED) as z:
        for path in sorted(items):
            z.write(path, path.relative_to(ROOT).as_posix())
    print(f"Pacote Roku criado: {TARGET} ({len(items)} arquivos)")


if __name__ == "__main__":
    main()
