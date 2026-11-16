"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import pivotal


def test_version_is_set() -> None:
    assert pivotal.__version__
