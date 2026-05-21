import sys
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).parent.parent))

from search.local_loader import load_local_sources


def test_load_local_sources_from_dir():
    with TemporaryDirectory() as td:
        base = Path(td)
        notes_dir = base / "notes"
        notes_dir.mkdir(parents=True)
        (notes_dir / "a.md").write_text("# A\nhello", encoding="utf-8")
        (notes_dir / "b.txt").write_text("world", encoding="utf-8")
        (notes_dir / "c.bin").write_bytes(b"\x00\x01")

        try:
            from pypdf import PdfWriter  # type: ignore
        except Exception:
            PdfWriter = None

        if PdfWriter:
            writer = PdfWriter()
            writer.add_blank_page(width=72, height=72)
            pdf_path = notes_dir / "d.pdf"
            with pdf_path.open("wb") as f:
                writer.write(f)

        items = load_local_sources(["notes"], base_dir=base, max_chars=100)
        urls = {x["url"] for x in items}
        assert "local://notes/a.md" in urls
        assert "local://notes/b.txt" in urls
        assert all("c.bin" not in u for u in urls)


if __name__ == "__main__":
    test_load_local_sources_from_dir()
    print("✅ local_loader tests passed.")
