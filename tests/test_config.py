"""Tests for config utility."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

# Ensure src package is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import src.config as config


def test_get_api_key_returns_value(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(config.ENV_API_KEY, "secret")
    assert config.get_api_key() == "secret"


def test_get_api_key_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(config.ENV_API_KEY, raising=False)
    with pytest.raises(RuntimeError):
        config.get_api_key()
