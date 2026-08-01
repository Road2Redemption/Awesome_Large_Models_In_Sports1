#!/usr/bin/env python3
"""Validate repository structure and the canonical taxonomy paper list."""

from __future__ import annotations

import re
import sys
import json
from html.parser import HTMLParser
from xml.etree import ElementTree
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ENTRY_RE = re.compile(
    r"^\d+\.\s+\*\*(?P<title>.+?)\*\*.*?"
    r"\[\[paper\]\(\s*(?P<url>https?://[^ )]+)\s*\)\]"
)


class CatalogHTMLValidator(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.local_references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        for attribute in ("href", "src"):
            value = values.get(attribute) or ""
            if value and "://" not in value and not value.startswith(("#", "mailto:")):
                self.local_references.append(value)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip().rstrip("/")


def main() -> int:
    errors: list[str] = []
    required_files = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "paper.bib",
        "CONTRIBUTING.md",
        "applications.jpg",
        "taxonomy.png",
        "docs/index.html",
        "docs/styles.css",
        "docs/app.js",
        "docs/papers.json",
        "docs/robots.txt",
        "docs/sitemap.xml",
        "docs/.nojekyll",
    ]

    for relative_path in required_files:
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    if errors:
        return report(errors)

    readme = README.read_text(encoding="utf-8")
    canonical = readme.split("## Year Index", 1)[0]
    section = "README introduction"
    seen: dict[tuple[str, str, str], int] = {}
    entry_count = 0

    for line_number, line in enumerate(canonical.splitlines(), 1):
        heading = re.match(r"^###\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1)

        if "[[paper](" not in line:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            errors.append(
                f"README.md:{line_number}: paper entry must contain a bold title "
                "and [[paper](https://...)]"
            )
            continue

        if line.count("**") != 2:
            errors.append(
                f"README.md:{line_number}: paper entry has malformed bold title markup"
            )

        entry_count += 1
        for field in ("title", "url"):
            value = normalize(match.group(field))
            key = (section, field, value)
            if key in seen:
                errors.append(
                    f"README.md:{line_number}: duplicate {field} in '{section}' "
                    f"(first seen on line {seen[key]})"
                )
            else:
                seen[key] = line_number

    if entry_count < 200:
        errors.append(
            f"canonical taxonomy unexpectedly contains only {entry_count} entries"
        )

    if "<!-- YEAR_INDEX:START -->" not in readme or "<!-- YEAR_INDEX:END -->" not in readme:
        errors.append("README is missing generated year-index markers")

    for image in re.findall(r'<img\s+[^>]*src="([^"]+)"', readme):
        if "://" not in image and not (ROOT / image).is_file():
            errors.append(f"README.md references missing image: {image}")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    required_citation_values = [
        "cff-version: 1.2.0",
        'title: "A Survey of Large Models in Sports"',
        "doi: 10.18653/v1/2026.findings-acl.1851",
        'url: "https://aclanthology.org/2026.findings-acl.1851/"',
    ]
    for value in required_citation_values:
        if value not in citation:
            errors.append(f"CITATION.cff is missing required metadata: {value}")

    bibtex = (ROOT / "paper.bib").read_text(encoding="utf-8")
    for value in (
        "@inproceedings{xu-etal-2026-survey,",
        "doi       = {10.18653/v1/2026.findings-acl.1851}",
        "pages     = {37154--37189}",
    ):
        if value not in bibtex:
            errors.append(f"paper.bib is missing official citation metadata: {value}")

    try:
        catalog = json.loads((ROOT / "docs/papers.json").read_text(encoding="utf-8"))
        if catalog.get("paper_count") != len(catalog.get("papers", [])):
            errors.append("docs/papers.json paper_count does not match its paper array")
        if catalog.get("paper_count", 0) < 200:
            errors.append("docs/papers.json contains unexpectedly few papers")
    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"docs/papers.json is invalid: {error}")

    catalog_html = CatalogHTMLValidator()
    catalog_html.feed((ROOT / "docs/index.html").read_text(encoding="utf-8"))
    if catalog_html.duplicate_ids:
        errors.append(
            "docs/index.html contains duplicate ids: "
            + ", ".join(sorted(catalog_html.duplicate_ids))
        )
    for reference in catalog_html.local_references:
        if not (ROOT / "docs" / reference).exists():
            errors.append(f"docs/index.html references missing local asset: {reference}")

    css = (ROOT / "docs/styles.css").read_text(encoding="utf-8")
    if css.count("{") != css.count("}"):
        errors.append("docs/styles.css contains unbalanced blocks")

    html = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    structured_data = re.search(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        html,
        re.DOTALL,
    )
    if not structured_data:
        errors.append("docs/index.html is missing scholarly JSON-LD metadata")
    else:
        try:
            json.loads(structured_data.group(1))
        except json.JSONDecodeError as error:
            errors.append(f"docs/index.html contains invalid JSON-LD: {error}")

    try:
        ElementTree.parse(ROOT / "docs/sitemap.xml")
    except ElementTree.ParseError as error:
        errors.append(f"docs/sitemap.xml is invalid: {error}")

    if errors:
        return report(errors)

    print(
        f"Repository validation passed: {entry_count} canonical entries, "
        f"{len(required_files)} required files, citation metadata verified."
    )
    return 0


def report(errors: list[str]) -> int:
    print("Repository validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
