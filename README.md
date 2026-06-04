# jcode-conf-py

Configuration path constants extracted from `jcode`. This library provides centralized path constants for Letta's global and per-project directories — including plugins, commands, history, and plans — so that all consumers share a single source of truth instead of hard-coding paths.

## Usage

```python
from jcode_conf import (
    LETTA_HOME,
    GLOBAL_CONFIG_DIR,
    GLOBAL_PLUGINS_DIR,
    GLOBAL_COMMANDS_DIR,
    GLOBAL_HISTORY_DIR,
    INSTALLED_PLUGINS_FILE,
    PROJECT_LETTA_DIR,
    PROJECT_COMMANDS_DIR,
    PROJECT_PLANS_DIR,
)

print(LETTA_HOME)            # ~/.letta (or $LETTA_HOME)
print(GLOBAL_COMMANDS_DIR)   # ~/.letta/commands
print(PROJECT_COMMANDS_DIR)  # .letta/commands
```

The `LETTA_HOME` root can be overridden via the `LETTA_HOME` environment variable.

## Build / Test / Install

```bash
just build    # uv build
just test     # uv run -m pytest
just install  # library package, no binary to install
```

## Installation

```bash
pip install jcode-conf-py
```
