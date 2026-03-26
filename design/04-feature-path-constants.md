# 路径常量系统

## 概述

提供 Letta 系统所需的所有标准路径常量，覆盖全局配置与项目级配置两大作用域。

## 概览

路径常量系统是本库的核心功能，通过集中定义路径常量，避免硬编码路径散落在依赖此库的其他组件中。所有常量均为 `pathlib.Path` 类型，支持跨平台路径操作。

## 设计意图

### 解决的问题

- 路径硬编码导致难以在不同环境（开发、测试、生产）间切换
- 不同组件使用不一致的路径约定
- 相对路径与绝对路径混用造成混乱

### 设计决策

- 使用 `pathlib.Path` 而非字符串：支持跨平台 `/` 操作符
- 全局路径绝对化：确保 I/O 操作可靠性
- 项目路径保持相对：支持项目级 `.letta` 目录的可移植性

## 架构

```mermaid
flowchart TB
    subgraph paths.py
        LH[LETTA_HOME<br/>Path] --> G1[GLOBAL_*<br/>Paths]
        G1 --> GP[GLOBAL_PLUGINS_DIR]
        G1 --> GC[GLOBAL_COMMANDS_DIR]
        G1 --> GH[GLOBAL_HISTORY_DIR]
        G1 --> GCfg[GLOBAL_CONFIG_DIR]

        P1[PROJECT_*<br/>Paths] --> PL[PROJECT_LETTA_DIR<br/>Path(".letta")]
        P1 --> PC[PROJECT_COMMANDS_DIR]
        P1 --> PP[PROJECT_PLANS_DIR]
    end
```

## 契约（Contract）

| 常量 | 类型 | 绝对/相对 | 运行时可修改 |
|------|------|-----------|--------------|
| `LETTA_HOME` | `Path` | 绝对 | ❌ 不可修改 |
| `GLOBAL_CONFIG_DIR` | `Path` | 绝对 | ❌ 不可修改 |
| `GLOBAL_PLUGINS_DIR` | `Path` | 绝对 | ❌ 不可修改 |
| `GLOBAL_COMMANDS_DIR` | `Path` | 绝对 | ❌ 不可修改 |
| `GLOBAL_HISTORY_DIR` | `Path` | 绝对 | ❌ 不可修改 |
| `PROJECT_LETTA_DIR` | `Path` | 相对 (`.letta`) | ❌ 不可修改 |
| `PROJECT_COMMANDS_DIR` | `Path` | 相对 (`.letta/commands`) | ❌ 不可修改 |
| `PROJECT_PLANS_DIR` | `Path` | 相对 (`.letta/plans`) | ❌ 不可修改 |
| `INSTALLED_PLUGINS_FILE` | `Path` | 绝对 | ❌ 不可修改 |

## API 参考

```python
from jcode_conf import (
    LETTA_HOME,
    GLOBAL_CONFIG_DIR,
    GLOBAL_PLUGINS_DIR,
    GLOBAL_COMMANDS_DIR,
    GLOBAL_HISTORY_DIR,
    PROJECT_LETTA_DIR,
    PROJECT_COMMANDS_DIR,
    PROJECT_PLANS_DIR,
    INSTALLED_PLUGINS_FILE,
)
```

| 参数 | 返回类型 | 说明 |
|------|----------|------|
| 所有导出常量 | `pathlib.Path` | 对应路径常量 |

## 集成矩阵

| 外部依赖 | 接口语义 | 失败策略 |
|----------|----------|----------|
| `pathlib.Path` | 标准库，无需接口 | N/A |
| `os.environ` | 读取 `LETTA_HOME` 环境变量 | 未设置时使用默认值 `~/.letta` |

## 使用示例

### 示例 1：访问全局命令目录

```python
from jcode_conf import GLOBAL_COMMANDS_DIR

# 列出全局命令
for cmd_file in GLOBAL_COMMANDS_DIR.glob("*.json"):
    print(cmd_file.name)
```

### 示例 2：构建项目级计划文件路径

```python
from jcode_conf import PROJECT_PLANS_DIR

plan_file = PROJECT_PLANS_DIR / "my_plan.md"
plan_file.write_text("# Plan\n\n- [ ] Task 1")
```

### 示例 3：检查插件清单

```python
from jcode_conf import INSTALLED_PLUGINS_FILE

if INSTALLED_PLUGINS_FILE.exists():
    import json
    with open(INSTALLED_PLUGINS_FILE) as f:
        plugins = json.load(f)
```

## 高级主题

### 路径计算细节

```python
# GLOBAL_PLUGINS_DIR 计算过程
LETTA_HOME = Path(os.environ.get("LETTA_HOME", Path.home() / ".letta"))
# 若 LETTA_HOME = ~/.letta，则
GLOBAL_PLUGINS_DIR = LETTA_HOME / "plugins"  # = ~/.letta/plugins
```

### 相对路径语义

`PROJECT_LETTA_DIR` 等项目级常量保持为相对路径 `Path(".letta")`，这意味着：
- 它们相对于**当前工作目录**（`os.getcwd()`）解析
- 适合在项目根目录执行的工具使用
- 不适合需要在任意目录执行的工具

## 限制与权衡

- **不支持动态更新**：路径常量在模块导入时固定，运行时修改 `LETTA_HOME` 不会影响已导入的常量
- **无路径验证**：不检查对应目录是否存在
- **无权限信息**：不提供路径的可读/可写状态

## 相关特性

- [环境变量覆盖](./05-feature-env-override.md) - `LETTA_HOME` 的环境变量配置机制
