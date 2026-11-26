"""Convert a Markdown script file to PDF using Python-Markdown and headless Chrome/Edge.

Usage:
    python tools/md_to_pdf.py <input.md> <output.pdf>

The pipeline's canonical deliverable remains the .md file. This helper only
produces a print-friendly PDF copy of that text — it never generates video.
"""

import html
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

CSS = """
@page { size: A4; margin: 16mm 14mm; }
body {
  font-family: "Segoe UI", "Nirmala UI", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  color: #1a1a1a;
}
h1 { font-size: 21pt; margin: 0 0 10pt; color: #111; }
h2 {
  font-size: 13pt;
  margin: 18pt 0 6pt;
  padding-bottom: 3pt;
  border-bottom: 1px solid #d0d0d0;
  color: #222;
  page-break-after: avoid;
}
h3 { font-size: 11pt; margin: 12pt 0 4pt; page-break-after: avoid; }
p, li { margin: 4pt 0; }
ul { margin: 4pt 0 8pt; padding-left: 18pt; }
blockquote {
  margin: 6pt 0;
  padding: 4pt 10pt;
  border-left: 3px solid #f5a623;
  background: #fff8ec;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 8pt 0 12pt;
  font-size: 9.5pt;
  page-break-inside: auto;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th, td {
  border: 1px solid #c8c8c8;
  padding: 5pt 6pt;
  text-align: left;
  vertical-align: top;
}
th { background: #f0f0f0; font-weight: 600; }
code {
  font-family: Consolas, "Courier New", monospace;
  background: #f4f4f4;
  padding: 0 2pt;
}
em { color: #555; }
hr { border: 0; border-top: 1px solid #ddd; margin: 14pt 0; }
"""

BROWSERS = [
    Path(os.environ.get("PROGRAMFILES", "")) / "Google/Chrome/Application/chrome.exe",
    Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Google/Chrome/Application/chrome.exe",
    Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Microsoft/Edge/Application/msedge.exe",
    Path(os.environ.get("PROGRAMFILES", "")) / "Microsoft/Edge/Application/msedge.exe",
]


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python md_to_pdf.py <input.md> <output.pdf>")
        return 2

    src = Path(sys.argv[1]).resolve()
    dst = Path(sys.argv[2]).resolve()
    if not src.is_file():
        print(f"Input not found: {src}")
        return 1
    dst.parent.mkdir(parents=True, exist_ok=True)

    body = markdown.markdown(
        src.read_text(encoding="utf-8"),
        extensions=["tables", "extra", "sane_lists", "fenced_code"],
    )
    document = (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(src.stem)}</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )

    browser = next((p for p in BROWSERS if p.is_file()), None)
    if browser is None:
        print("No Chrome or Edge executable found.")
        return 1

    with tempfile.TemporaryDirectory(prefix="md2pdf-") as tmp:
        html_path = Path(tmp) / "script.html"
        html_path.write_text(document, encoding="utf-8")
        profile = Path(tmp) / "profile"
        cmd = [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            f"--user-data-dir={profile}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={dst}",
            html_path.as_uri(),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    if not dst.is_file() or dst.stat().st_size == 0:
        print("PDF was not created.")
        print(result.stdout.strip())
        print(result.stderr.strip())
        return 1

    print(f"PDF created: {dst} ({dst.stat().st_size:,} bytes) using {browser.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
