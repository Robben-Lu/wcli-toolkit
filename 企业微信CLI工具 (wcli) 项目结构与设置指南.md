# 企业微信CLI工具 (wcli) 项目结构与设置指南

## 1. 项目文件结构

这是推荐的项目结构，它遵循了Python社区的最佳实践，将源代码、测试和配置清晰地分离开。

wcli-toolkit/
├── .vscode/
│   └── settings.json       # VS Code工作区配置，用于自动格式化和Linting
├── wcli/                   # 主源代码包
│   ├── __init__.py
│   ├── main.py             # Typer App的入口文件，定义CLI命令结构
│   ├── core/               # 核心逻辑模块
│   │   ├── __init__.py
│   │   ├── client.py       # 封装wechatpy的客户端，处理认证和token
│   │   ├── logger.py       # 日志配置和管理
│   │   ├── security.py    # 密钥管理，使用keyring存储敏感信息
│   │   └── response.py    # 统一响应格式定义
│   ├── commands/           # 存放所有CLI子命令的模块
│   │   ├── __init__.py
│   │   ├── config.py       # 实现 'wcli config ...' 配置相关命令
│   │   ├── user.py         # 实现 'wcli user ...' 相关命令
│   │   ├── department.py   # 实现 'wcli department ...' 相关命令
│   │   ├── msg.py          # 实现 'wcli msg ...' 相关命令
│   │   └── group.py        # 实现 'wcli group ...' 群聊管理命令
│   ├── config.py           # 配置加载和管理模块
│   └── utils/              # 工具函数
│       ├── __init__.py
│       └── retry.py        # 重试装饰器和相关工具

├── tests/                  # 测试代码目录
│   ├── __init__.py
│   └── test_user_commands.py # 针对user命令的测试用例
├── .gitignore              # Git忽略文件配置
├── .pre-commit-config.yaml # pre-commit hooks配置
├── pyproject.toml          # 项目元数据和依赖管理 (使用Poetry)
├── README.md               # 项目说明文档
└── config.example.yaml     # 配置文件示例，用于向用户展示格式

## 2. 在VS Code中创建和设置项目的步骤

请按以下步骤操作，即可在您的本地环境中完整地搭建起项目。

### 步骤一：创建项目目录和文件

在您的终端中，执行以下命令来创建所有必需的文件夹和空文件。

```bash
# 创建项目根目录并进入
mkdir wcli-toolkit
cd wcli-toolkit

# 创建源代码目录结构
mkdir -p wcli/core wcli/commands wcli/utils tests

# 创建空的Python文件
touch wcli/__init__.py wcli/main.py wcli/config.py
touch wcli/core/__init__.py wcli/core/client.py wcli/core/logger.py wcli/core/security.py wcli/core/response.py
touch wcli/commands/__init__.py wcli/commands/config.py wcli/commands/user.py wcli/commands/department.py wcli/commands/msg.py wcli/commands/group.py
touch wcli/utils/__init__.py wcli/utils/retry.py
touch tests/__init__.py tests/test_user_commands.py

# 创建配置文件和文档
touch .gitignore README.md config.example.yaml .pre-commit-config.yaml

# 创建VS Code配置目录和文件
mkdir .vscode
touch .vscode/settings.json
```

### 步骤二：配置项目 (pyproject.toml)

这是项目的核心配置文件，使用 [Poetry](https://python-poetry.org/) 进行管理。如果您没有安装Poetry，请先安装它。

将以下内容复制到 `pyproject.toml` 文件中：

```toml
[tool.poetry]
name = "wcli"
version = "0.1.0"
description = "A CLI toolkit for WeCom (Enterprise WeChat) to be used by AI agents and humans."
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{include = "wcli"}]

[tool.poetry.dependencies]
python = "^3.9"
typer = {extras = ["all"], version = "^0.12.3"}
wechatpy = "^2.0.0"
pyyaml = "^6.0.1"
rich = "^13.7.1"  # Typer的好搭档，用于美化输出和进度条
keyring = "^24.3.0"  # 安全存储敏感信息
tenacity = "^8.2.3"  # 重试机制
questionary = "^2.0.1"  # 交互式配置向导

[tool.poetry.dev-dependencies]
pytest = "^8.2.2"
black = "^24.4.2"
ruff = "^0.4.8"
pre-commit = "^3.7.1"

[tool.poetry.scripts]
# 这允许你安装后直接在命令行使用 'wcli' 命令
wcli = "wcli.main:app"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.main.api"
```

### 步骤三：安装依赖

在项目根目录 (`wcli-toolkit/`) 下打开终端，运行Poetry来创建虚拟环境并安装所有依赖。

```bash
# Poetry会自动创建一个虚拟环境并安装所有在pyproject.toml中定义的库
poetry install
```

### 步骤四：配置VS Code (`.vscode/settings.json`)

将以下内容复制到 `.vscode/settings.json`。这会告诉VS Code在保存文件时自动使用Black进行格式化，并使用Ruff进行代码检查，同时指向Poetry创建的虚拟环境。

```json
{
    // 自动发现并使用Poetry的虚拟环境
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,

    // 保存时自动格式化
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": true
        }
    },
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true
}
```
*注意: VS Code可能会提示您安装Python、Black Formatter和Ruff扩展，请务必安装。*

### 步骤五：配置示例文件

1.  **.gitignore**: 将常见的Python忽略项添加进去。可以从 [github/gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore) 复制。

2.  **config.example.yaml**: 添加示例配置内容。
    ```yaml
    # 企业微信凭证配置
    # 首次运行 'wcli config init' 或 'wcli config init --interactive' 时会自动创建 ~/.wcli/config.yaml
    # 注意：敏感信息（如Secret）将存储在系统密钥链中，不会保存在此文件
    wcli:
      corpid: "YOUR_CORP_ID_HERE" # 你的企业ID
      # 应用配置
      apps:
        contact:
          agent_id: 1000001  # 通讯录应用ID
        message:
          agent_id: 1000002  # 消息应用ID
      # 默认设置
      defaults:
        output_format: "json"  # 默认输出格式: json, table, text
        log_level: "INFO"  # 日志级别: DEBUG, INFO, WARNING, ERROR
    ```

3.  **.pre-commit-config.yaml**: 添加pre-commit hooks配置。
    ```yaml
    repos:
      - repo: https://github.com/psf/black
        rev: 24.4.2
        hooks:
          - id: black
            language_version: python3.9
      - repo: https://github.com/charliermarsh/ruff-pre-commit
        rev: v0.4.8
        hooks:
          - id: ruff
            args: [--fix]
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.6.0
        hooks:
          - id: trailing-whitespace
          - id: end-of-file-fixer
          - id: check-yaml
          - id: check-added-large-files
    ```

### 步骤六：安装pre-commit hooks

在项目根目录下运行以下命令来安装pre-commit hooks：

```bash
# 安装pre-commit hooks
poetry run pre-commit install

# 可选：立即对所有文件运行hooks进行检查
poetry run pre-commit run --all-files
```

### 完成！

现在，您的项目已经完全设置好了。您可以在VS Code中打开 `wcli-toolkit` 文件夹，它会自动激活配置好的Python环境和工具。每次提交代码时，pre-commit hooks会自动运行格式化和代码检查。您可以开始在 `wcli/main.py` 中编写您的第一个CLI命令了！

## 3. 关键模块说明

### 3.1 核心模块 (wcli/core/)

- **client.py**: 封装wechatpy客户端，处理token缓存和自动刷新
- **logger.py**: 配置日志系统，支持不同级别的日志输出
- **security.py**: 使用keyring安全存储和读取敏感信息
- **response.py**: 定义统一的响应格式，确保输出一致性

### 3.2 命令模块 (wcli/commands/)

- **config.py**: 配置管理命令，包括交互式初始化向导
- **user.py**: 用户管理相关命令
- **department.py**: 部门管理相关命令
- **msg.py**: 消息发送相关命令
- **group.py**: 群聊管理相关命令

### 3.3 工具模块 (wcli/utils/)

- **retry.py**: 基于tenacity的重试装饰器，处理网络请求失败
