from __future__ import annotations

from pathlib import Path


_TEXT_EXTS = {".md", ".markdown", ".txt"}
_PDF_EXTS = {".pdf"}


def _iter_input_paths(inputs: list[str], base_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for raw in inputs:
        p = Path(raw)
        if not p.is_absolute():
            p = (base_dir / p).resolve()
        if p.exists():
            paths.append(p)
    return paths


def _read_pdf_text(path: Path, max_chars: int) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return ""

    try:
        reader = PdfReader(str(path))
    except Exception:
        return ""

    parts: list[str] = []
    total = 0
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if not text:
            continue
        parts.append(text)
        total += len(text)
        if total >= max_chars:
            break

    return "\n".join(parts)[:max_chars]


def load_local_sources(
    inputs: list[str],
    base_dir: Path,
    max_chars: int = 4000,
) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    seen: set[str] = set()

    for p in _iter_input_paths(inputs, base_dir):
        candidates: list[Path]
        if p.is_dir():
            candidates = [
                x
                for x in p.rglob("*")
                if x.is_file() and (x.suffix.lower() in _TEXT_EXTS or x.suffix.lower() in _PDF_EXTS)
            ]
        else:
            candidates = [p] if (p.suffix.lower() in _TEXT_EXTS or p.suffix.lower() in _PDF_EXTS) else []

        for file_path in candidates:
            try:
                rel = file_path.resolve().relative_to(base_dir.resolve())
            except Exception:
                rel = file_path.name

            rel_str = str(rel).replace('\\', '/')
            url = f"local://{rel_str}"
            if url in seen:
                continue
            seen.add(url)

            if file_path.suffix.lower() in _PDF_EXTS:
                text = _read_pdf_text(file_path, max_chars=max_chars)
            else:
                try:
                    text = file_path.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    continue

            if not text.strip():
                continue

            snippet = text.strip().replace("\r\n", "\n")[:max_chars]
            title = file_path.stem
            items.append({"url": url, "title": title, "snippet": snippet})

    return items
