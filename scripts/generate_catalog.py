#!/usr/bin/env python3
"""Generate the searchable web catalog data from README taxonomy entries."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "docs" / "papers.json"
ENTRY_RE = re.compile(
    r"^\d+\.\s+\*\*(?P<title>.+?)\*\*"
    r"(?P<metadata>.*?)\[\[paper\]\(\s*(?P<url>https?://[^ )]+)\s*\)\]"
    r"(?P<resources>.*)$"
)
RESOURCE_RE = re.compile(r"\[\[(?P<kind>code|dataset|model|project)\]\((?P<url>https?://[^ )]+)\)\]")
YEAR_RE = re.compile(r"\b(20\d{2})\b")
ARXIV_YEAR_RE = re.compile(r"arxiv(?::|\.org/(?:abs|pdf)/)(\d{2})", re.IGNORECASE)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def infer_year(metadata: str, line: str) -> int | None:
    years = YEAR_RE.findall(metadata)
    if years:
        return int(years[-1])
    arxiv = ARXIV_YEAR_RE.search(line)
    return int(f"20{arxiv.group(1)}") if arxiv else None


def parse_catalog(readme: str) -> list[dict[str, object]]:
    canonical = readme.split("## Year Index", 1)[0]
    stakeholder = ""
    topic = ""
    papers: OrderedDict[str, dict[str, object]] = OrderedDict()

    for line in canonical.splitlines():
        h2 = re.match(r"^##\s+(.+?)\s*$", line)
        if h2:
            heading = h2.group(1)
            if heading.startswith("Applications for ") or heading in {
                "Sports Understanding",
                "Related Surveys",
            }:
                stakeholder = heading
                topic = ""
            continue

        h3 = re.match(r"^###\s+(.+?)\s*$", line)
        if h3 and stakeholder:
            topic = h3.group(1)
            continue

        if "[[paper](" not in line or not stakeholder:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            continue

        title = match.group("title").strip()
        key = normalize(title)
        category = {"stakeholder": stakeholder, "topic": topic or stakeholder}
        if key in papers:
            categories = papers[key]["categories"]
            if category not in categories:
                categories.append(category)
            continue

        metadata = match.group("metadata").strip().lstrip(",").strip()
        resources = {
            item.group("kind"): item.group("url")
            for item in RESOURCE_RE.finditer(match.group("resources"))
        }
        papers[key] = {
            "title": title,
            "year": infer_year(metadata, line),
            "venue": metadata,
            "paper": match.group("url"),
            "resources": resources,
            "categories": [category],
        }

    return list(papers.values())


def serialized_catalog() -> str:
    papers = parse_catalog(README.read_text(encoding="utf-8"))
    payload = {
        "generated_from": "README.md",
        "paper_count": len(papers),
        "papers": papers,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = serialized_catalog()

    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != generated:
            print(
                "docs/papers.json is stale; run `python3 scripts/generate_catalog.py`.",
                file=sys.stderr,
            )
            return 1
        print("Search catalog data is up to date.")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Generated searchable catalog with {len(json.loads(generated)['papers'])} papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
