# Literature Search Protocol

This repository is a living bibliography. The current update covers papers first made public from **July 1, 2025 through July 31, 2026**.

## Sources

- [arXiv](https://arxiv.org/) for primary preprint records and first-submission dates.
- [alphaXiv](https://www.alphaxiv.org/) for discovery and full-text cross-checking of arXiv papers.
- [SportRxiv](https://sportrxiv.org/) for sport, exercise, performance, and health preprints.

Searches combined the survey taxonomy with large-model terms, including `LLM`, `MLLM`, `VLM`, `Video-LLM`, `ChatGPT`, `RAG`, and `agent`, and sport/task terms covering coaching, training, action assessment, tactics, refereeing, commentary, highlights, media, scouting, wearables, and sports understanding.

## Inclusion Rules

A paper is included when:

1. its first public release falls inside the update window;
2. an LLM, MLLM, VLM, or closely related large-model system is central to the sports task, dataset, benchmark, or analysis; and
3. a stable primary paper or preprint page is available.

Later revisions of papers first released before July 1, 2025 are not counted as new papers. Traditional machine-learning papers without a central large-model component, papers that only mention sport as an incidental example, and papers that only disclose using generative AI for writing assistance are excluded.

## Current Update

The August 1, 2026 refresh adds **18 unique papers** to the taxonomy: **6 first released in 2025** and **12 first released in 2026**. Papers assigned to multiple taxonomy topics remain a single record in the searchable catalog.

The canonical records live in [README.md](README.md). After editing them, regenerate the derived views with:

```bash
python3 scripts/generate_year_index.py
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
```
