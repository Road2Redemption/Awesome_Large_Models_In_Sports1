# Contributing

Thank you for helping keep Awesome Large Models in Sports accurate and useful.

## What belongs in this list

A contribution should have a clear connection to both large models and sports. We welcome peer-reviewed papers, high-quality preprints, datasets, benchmarks, open-source models, and deployed systems.

Traditional machine learning work without a large language, vision-language, multimodal, or foundation-model component is outside the current scope. General video-language work should be included only when it provides a method or benchmark directly useful for sports understanding.

## Before submitting

1. Search `README.md` for the exact title, DOI, arXiv identifier, and URL.
2. Choose the single most relevant taxonomy section.
3. Prefer an ACL Anthology, publisher, DOI, OpenReview, or arXiv abstract page over aggregators and direct PDF links.
4. Confirm the title, venue, and year against the linked source.
5. Use the paper request issue form if you are unsure about the category.

## Entry format

```markdown
1. **Paper Title**, Venue Year [[paper](https://canonical-paper-link)] [[code](https://github.com/owner/repository)] [[dataset](https://dataset-link)]
```

Only the paper link is required. Add `code`, `dataset`, `model`, or `project` links when official resources are available. Do not add promotional descriptions or citation counts.

## Pull requests

- Keep one paper or one focused correction per pull request when possible.
- Add new entries at the end of the relevant taxonomy subsection.
- Do not manually add an entry to the generated year index.
- Do not renumber an entire section; Markdown renders repeated `1.` markers correctly.
- Explain in one sentence why the selected category is appropriate.
- Run `python3 scripts/generate_year_index.py` after changing paper entries.
- Run `python3 scripts/generate_catalog.py` to update the searchable web catalog.
- Run `python3 scripts/validate_repository.py` before submitting.

Maintainers may edit titles, metadata, links, or categories to keep the collection consistent. Inclusion is based on relevance and verifiable scholarly value, not on author affiliation.

## Corrections and new categories

For broken links or metadata errors, use the correction issue form or submit a focused pull request. Proposals for new categories should include at least three representative works and explain why the existing taxonomy does not cover them.
