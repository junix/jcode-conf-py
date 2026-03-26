# API 参考与使用

## 概述

`jcode-conf-py` 提供极简公共 API：通过 `import` 访问导出常量。无需实例化或初始化。

## 入门

```python
from jcode_conf import (
    LETTA_HOME,
    GLOBAL_COMMANDS_DIR,
    GLOBAL_PLUGINS_DIR,
    PROJECT_COMMANDS_DIR,
    PROJECT_LETTA_DIR,
)
```

说明：直接从包层级导入所需常量，无需任何配置步骤。

## 核心 API

### 顶层导入

| 导出项 | 类型 | 说明 | 位置 |
|--------|------|------|------|
| `LETTA_HOME` | `Path` | 全局配置根目录（绝对路径） | `paths.py:6` |
| `GLOBAL_CONFIG_DIR` | `Path` | 等于 `LETTA_HOME` | `paths.py:8` |
| `GLOBAL_PLUGINS_DIR` | `Path` | 全局插件目录 | `paths.py:9` |
| `GLOBAL_COMMANDS_DIR` | `Path` | 全局命令目录 | `paths.py:10` |
| `GLOBAL_HISTORY_DIR` | `Path` | 全局历史记录目录 | `paths.py:11` |
| `PROJECT_LETTA_DIR` | `Path` | 项目 `.letta` 目录（相对） | `paths.py:13` |
| `PROJECT_COMMANDS_DIR` | `Path` | 项目命令目录（相对） | `paths.py:14` |
| `PROJECT_PLANS_DIR` | `Path` | 项目计划目录（相对） | `paths.py:15` |
| `INSTALLED_PLUGINS_FILE` | `Path` | 已安装插件清单 JSON | `paths.py:17` |

## 常见模式

### 模式 1：读取全局配置

```python
from jcode_conf import GLOBAL_CONFIG_DIR

config_file = GLOBAL_CONFIG_DIR / "config.json"
```

### 模式 2：构建项目路径

```python
from jcode_conf import PROJECT_LETTA_DIR, PROJECT_COMMANDS_DIR

# 创建项目级 .letta 目录下的子目录
commands_dir = PROJECT_COMMANDS_DIR
```

### 模式 3：环境覆盖

```bash
export LETTA_HOME=/custom/path
python -c "from jcode_conf import LETTA_HOME; print(LETTA_HOME)"
# 输出：/custom/path
```

说明：设置 `LETTA_HOME` 环境变量后，所有全局路径自动基于新值计算。

## 配置

| 环境变量 | 默认值 | 影响范围 |
|----------|--------|----------|
| `LETTA_HOME` | `~/.letta` | 所有 `GLOBAL_*` 路径常量 |

## 最佳实践

- ✅ 导入时直接使用常量，不做二次赋值
- ✅ 全局路径只读，勿在运行时修改 `LETTA_HOME`
- ✅ 项目路径保持相对性，适配多项目场景
- ❌ 不要将 `LETTA_HOME` 的返回值与字符串拼接，应使用 `/` 路径操作
