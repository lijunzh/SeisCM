# Contributing to SeisCM

Thanks for your interest! Bug reports, new colormaps and documentation
improvements are all welcome.

## Getting started

```bash
git clone https://github.com/lijunzh/SeisCM.git
cd SeisCM
uv sync --dev
uv run pre-commit install
```

## Before opening a pull request

```bash
uv run ruff check src tests
uv run ruff format src tests
uv run mypy
uv run pytest --cov
```

- Add or update tests for any behaviour change.
- Add an entry under **Unreleased** in `CHANGELOG.md`.
- Keep pull requests focused; one logical change per PR.

## Adding a colormap

1. Add a function returning a `LinearSegmentedColormap` in
   `src/seiscm/seiscm.py` with a NumPy-style docstring.
2. Export it from `src/seiscm/__init__.py` and add it to `__all__`.
3. Add tests and a row to the table in `README.md` (and regenerate
   `fig/colormaps.png` if practical).

## Releasing (maintainers)

Versions come from git tags via `setuptools-scm`. Update the changelog, then
push a tag such as `v1.2.3`; CI publishes to PyPI and creates a GitHub release.

By contributing you agree that your contributions are licensed under the
MIT License and that you will follow the [Code of Conduct](CODE_OF_CONDUCT.md).
