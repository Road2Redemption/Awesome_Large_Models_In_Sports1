# Literature Search Protocol

This repository is a living bibliography. The current update covers papers first made public from **July 1, 2025 through July 31, 2026**.

## Sources

- [arXiv](https://arxiv.org/) for primary preprint records and first-submission dates.
- [alphaXiv](https://www.alphaxiv.org/) for discovery and full-text cross-checking of arXiv papers.
- [SportRxiv](https://sportrxiv.org/) for sport, exercise, performance, and health preprints.

Searches combined the survey taxonomy with large-model terms, including `LLM`, `MLLM`, `VLM`, `Video-LLM`, `ChatGPT`, `RAG`, and `agent`, and sport/task terms covering coaching, training, action assessment, tactics, refereeing, commentary, highlights, media, scouting, wearables, and sports understanding. Titles and keyword matches are used only to retrieve candidates; every candidate is screened from its abstract, with the methods section consulted when the abstract does not establish the model's role.

## Inclusion Rules

A paper is included when:

1. its first public release falls inside the update window;
2. an LLM, MLLM, VLM, or closely related large-model system is central to the sports task, dataset, benchmark, or analysis; and
3. a stable primary paper or preprint page is available.

Later revisions of papers first released before July 1, 2025 are not counted as new papers. Traditional machine-learning papers without a central large-model component, papers that only mention sport as an incidental example, papers that mention LLMs only as future work, and papers that only disclose using generative AI for writing assistance are excluded.

## Screening Audit

The screening decision is based on what the abstract says the paper actually does, not on title similarity. Examples from this refresh:

| Candidate | Decision | Abstract-level reason |
| --- | --- | --- |
| **TennisTV** (arXiv:2509.15602) | Include | Introduces a tennis benchmark and evaluates 17 MLLMs across eight rally-understanding tasks. |
| **SPORTSQL** (arXiv:2508.17157) | Include | Uses LLMs for sports query parsing, schema linking, and visualization selection, and contributes a 1,700-query benchmark. |
| **RAG-HAR+** (arXiv:2607.26631) | Exclude | The six general HAR benchmarks are not presented as sports research; fitness is only one possible application. |
| **Using LLMs for Late Multimodal Sensor Fusion for Activity Recognition** (arXiv:2509.10729) | Exclude | Sport is one activity context in a general Ego4D subset rather than the research domain. |
| **Right Move, Right Time** (SportRxiv 749) | Exclude | The abstract describes spatial evaluation methods without a central large-model component. |
| **Beyond the Metrics** (SportRxiv 850) | Exclude | The study uses manual content and sentiment analysis; LLM analysis appears only as future work. |

## Current Update

The August 1, 2026 refresh adds **38 unique papers** to the taxonomy: **17 first released in 2025** and **21 first released in 2026**. Papers assigned to multiple taxonomy topics remain a single record in the searchable catalog.

The canonical records live in [README.md](README.md). After editing them, regenerate the derived views with:

```bash
python3 scripts/generate_year_index.py
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
```
