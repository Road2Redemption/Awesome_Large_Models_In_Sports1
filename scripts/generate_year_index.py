#!/usr/bin/env python3
"""Generate the README year index from the canonical taxonomy sections."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX_HEADING = "## Year Index"
CONTRIBUTION_HEADING = "## 🤝 Contribution"
ENTRY_RE = re.compile(r"^\d+\.\s+\*\*(?P<title>.+?)\*\*")
YEAR_RE = re.compile(r"\b(20\d{2})\b")
ARXIV_YEAR_RE = re.compile(r"arxiv(?::|\.org/(?:abs|pdf)/)(\d{2})", re.IGNORECASE)


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.casefold()).strip()


def build_index(canonical: str) -> str:
    by_year: dict[str, list[str]] = defaultdict(list)
    unknown: list[str] = []
    seen_titles: set[str] = set()

    for line in canonical.splitlines():
        if "[[paper](" not in line:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            continue

        title_key = normalize_title(match.group("title"))
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)

        metadata = line.split("[[paper](", 1)[0]
        years = YEAR_RE.findall(metadata)
        if not years:
            arxiv_year = ARXIV_YEAR_RE.search(line)
            if arxiv_year:
                years = [f"20{arxiv_year.group(1)}"]
        normalized_line = re.sub(r"^\d+\.", "1.", line, count=1).rstrip()
        if years:
            by_year[years[-1]].append(normalized_line)
        else:
            unknown.append(normalized_line)

    lines = [
        INDEX_HEADING,
        "",
        "> This index is generated from the taxonomy above. Do not edit it manually; run `python3 scripts/generate_year_index.py` after changing paper entries.",
        "",
        "<!-- YEAR_INDEX:START -->",
    ]

    for year in sorted(by_year, reverse=True):
        lines.extend(["", f"### {year}", "", *by_year[year]])

    if unknown:
        lines.extend(["", "### Year not specified", "", *unknown])

    lines.extend(["", "<!-- YEAR_INDEX:END -->", ""])
    return "\n".join(lines)


def render(readme: str) -> str:
    if INDEX_HEADING not in readme or CONTRIBUTION_HEADING not in readme:
        raise ValueError("README is missing the year index or contribution heading")

    canonical, remainder = readme.split(INDEX_HEADING, 1)
    _, footer = remainder.split(CONTRIBUTION_HEADING, 1)
    return canonical.rstrip() + "\n\n" + build_index(canonical) + "\n" + CONTRIBUTION_HEADING + footer


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when README does not contain the generated year index",
    )
    args = parser.parse_args()

    current = README.read_text(encoding="utf-8")
    try:
        generated = render(current)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if args.check:
        if current != generated:
            print(
                "README year index is stale; run "
                "`python3 scripts/generate_year_index.py`.",
                file=sys.stderr,
            )
            return 1
        print("Generated year index is up to date.")
        return 0

    README.write_text(generated, encoding="utf-8")
    print("Updated README year index from canonical taxonomy entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
