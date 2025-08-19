import sys
import pytest

from py_core_to_cloud import __main__


def test_main_with_name(capsys, monkeypatch):
    # Simulate CLI args: python -m py_core_to_cloud --name Python
    monkeypatch.setattr(sys, "argv", ["prog", "--name", "Python"])
    __main__.main()
    captured = capsys.readouterr()
    assert "Hello, Python!" in captured.out


def test_main_default(capsys, monkeypatch):
    # Simulate CLI args: python -m py_core_to_cloud
    monkeypatch.setattr(sys, "argv", ["prog"])
    __main__.main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
