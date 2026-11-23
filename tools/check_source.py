"""Checagem estática básica: XML, JSON, referências e padrões de credenciais."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["manifest", "LICENSE", "source/main.brs", "components/MainScene.xml"]
EXTENSIONS = {".brs", ".xml", ".json", ".html", ".txt"}
SENSITIVE_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "cloud credential": re.compile(r"(?:sk-[A-Za-z0-9_-]{24,}|AIza[0-9A-Za-z_-]{30,}|xox[baprs]-[0-9A-Za-z-]{20,}|AKIA[0-9A-Z]{16})"),
    "embedded bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._-]{25,}", re.I),
}
PKG_RE = re.compile(r"pkg:/([A-Za-z0-9_./\-]+)")


def main() -> None:
    errors = []
    count = {"xml": 0, "json": 0, "files": 0}
    for f in REQUIRED:
        if not (ROOT / f).is_file():
            errors.append(f"Arquivo essencial ausente: {f}")
    for f in sorted(ROOT.rglob("*")):
        if not f.is_file() or "dist" in f.relative_to(ROOT).parts or ".git" in f.relative_to(ROOT).parts:
            continue
        count["files"] += 1
        if f.suffix.lower() == ".xml":
            try:
                ET.parse(f)
                count["xml"] += 1
            except ET.ParseError as exc:
                errors.append(f"XML inválido: {f.relative_to(ROOT)} ({exc})")
        if f.suffix.lower() == ".json":
            try:
                json.loads(f.read_text(encoding="utf-8"))
                count["json"] += 1
            except (ValueError, UnicodeError) as exc:
                errors.append(f"JSON inválido: {f.relative_to(ROOT)} ({exc})")
        if f.suffix.lower() not in EXTENSIONS and f.name != "manifest":
            continue
        # Só varrer código e metadados; os documentos explicativos podem citar
        # nomes de padrões maliciosos sem conter segredos verdadeiros.
        if not any(part in ("source", "components", "web", "locale") for part in f.relative_to(ROOT).parts) and f.name != "manifest":
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        for label, regex in SENSITIVE_PATTERNS.items():
            if regex.search(text):
                errors.append(f"Padrão sensível ({label}): {f.relative_to(ROOT)}")
        for found in PKG_RE.findall(text):
            if found.endswith("/") or ".." in Path(found).parts:
                continue
            # Descarta placeholders de URI com concatenação dinâmica
            if found.startswith(("http", "storage", "fonts")):
                continue
            rel = Path(found)
            if not (ROOT / rel).is_file() and not (ROOT / rel).is_dir():
                # Aviso em vez de falha para caminhos construídos parcialmente
                # em tempo de execução (p.ex. pkg:/images/ + nome do arquivo).
                print(f"AVISO: recurso não literal / dinâmico: {f.relative_to(ROOT)} -> {found}")
    print(f"Arquivos: {count['files']}; XMLs válidos: {count['xml']}; JSONs válidos: {count['json']}")
    if errors:
        for error in sorted(set(errors)):
            print("ERRO:", error)
        sys.exit(1)
    print("Checagem estática básica concluída (não substitui teste no Roku).")


if __name__ == "__main__":
    main()
