"""Letta centralized path constants."""

import os
from pathlib import Path

_default_letta_home = Path.home() / ".letta"
LETTA_HOME = Path(os.environ.get("LETTA_HOME", _default_letta_home)).expanduser().resolve()

GLOBAL_CONFIG_DIR = LETTA_HOME
GLOBAL_PLUGINS_DIR = LETTA_HOME / "plugins"
GLOBAL_COMMANDS_DIR = LETTA_HOME / "commands"
GLOBAL_HISTORY_DIR = LETTA_HOME / "history"

PROJECT_LETTA_DIR = Path(".letta")
PROJECT_COMMANDS_DIR = PROJECT_LETTA_DIR / "commands"
PROJECT_PLANS_DIR = PROJECT_LETTA_DIR / "plans"

INSTALLED_PLUGINS_FILE = GLOBAL_PLUGINS_DIR / "installed_plugins.json"

__all__ = [
    "GLOBAL_COMMANDS_DIR",
    "GLOBAL_CONFIG_DIR",
    "GLOBAL_HISTORY_DIR",
    "GLOBAL_PLUGINS_DIR",
    "INSTALLED_PLUGINS_FILE",
    "LETTA_HOME",
    "PROJECT_COMMANDS_DIR",
    "PROJECT_LETTA_DIR",
    "PROJECT_PLANS_DIR",
]
