from __future__ import annotations

from pathlib import Path

from jcode_conf.paths import LETTA_HOME, PROJECT_COMMANDS_DIR, PROJECT_LETTA_DIR, PROJECT_PLANS_DIR


def test_project_paths_remain_relative() -> None:
    assert PROJECT_LETTA_DIR == Path(".letta")
    assert PROJECT_COMMANDS_DIR == Path(".letta/commands")
    assert PROJECT_PLANS_DIR == Path(".letta/plans")


def test_letta_home_is_resolved_path() -> None:
    assert LETTA_HOME.is_absolute()
