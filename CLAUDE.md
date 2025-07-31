# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

wcli (WeCom CLI Toolkit) is a command-line tool designed to interface with WeCom (Enterprise WeChat) APIs. The primary purpose is to serve as a bridge between AI agents (like Google Gemini or Claude) and the WeCom platform, enabling automated management tasks through natural language instructions.

## Development Commands

### Setup & Installation
```bash
# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies and create virtual environment
poetry install

# Activate the virtual environment
poetry shell

# Install pre-commit hooks
poetry run pre-commit install
```

### Development Commands
```bash
# Run the CLI tool
poetry run wcli [command]

# Or after installation as a script
wcli [command]

# Run tests
poetry run pytest

# Format code with Black
poetry run black wcli tests

# Lint code with Ruff
poetry run ruff wcli tests

# Run all pre-commit hooks manually
poetry run pre-commit run --all-files

# Type checking (if mypy is added)
poetry run mypy wcli
```

### Building & Distribution
```bash
# Build the package
poetry build

# Install the package locally for testing
poetry install
```

## Architecture

### Core Components

1. **CLI Framework**: Built on Typer for command structure and argument parsing
2. **WeCom SDK**: Uses wechatpy library for API interactions  
3. **Security**: Keyring for secure credential storage
4. **Configuration**: YAML-based config in ~/.wcli/config.yaml (non-sensitive data only)
5. **Logging**: Python logging module with configurable levels
6. **Retry Logic**: Tenacity for automatic retries with backoff
7. **Progress Display**: Rich for progress bars and formatted output

### Module Structure

- **wcli/main.py**: Entry point defining the CLI app and command groups
- **wcli/config.py**: Configuration loading and management
- **wcli/core/**: Core functionality modules
  - **client.py**: Encapsulates wechatpy client, handles authentication and token management
  - **logger.py**: Logging configuration and utilities
  - **security.py**: Keyring integration for secure credential storage
  - **response.py**: Unified response format definition
- **wcli/commands/**: Individual command modules
  - **config.py**: Configuration commands including interactive setup
  - **user.py**: User management commands
  - **department.py**: Department management commands
  - **msg.py**: Message sending commands
  - **group.py**: Group chat management commands
- **wcli/utils/**: Utility modules
  - **retry.py**: Retry decorators and utilities

### Key Design Principles

1. **AI-Friendly Output**: All commands support `--output json` for machine-readable responses
2. **Unified Response Format**: Consistent JSON structure with success/error/data fields
3. **Error Handling**: Non-zero exit codes on failure, errors to stderr, results to stdout
4. **Security**: Sensitive credentials stored in system keyring, never in files or logs
5. **Modularity**: Each API domain has its own command module
6. **Reliability**: Automatic retries, progress indicators, comprehensive logging

## Configuration

The tool uses a two-tier configuration approach:
1. **~/.wcli/config.yaml**: Non-sensitive configuration (corpid, app IDs, preferences)
2. **System Keyring**: Sensitive data (secrets, tokens) via keyring library

Example config.yaml:
```yaml
wcli:
  corpid: "YOUR_CORP_ID"
  apps:
    contact:
      agent_id: 1000001
    message:
      agent_id: 1000002
  defaults:
    output_format: "json"
    log_level: "INFO"
```

## Testing Strategy

- Unit tests in `tests/` directory using pytest
- Tests should mock WeCom API calls to avoid requiring real credentials
- Focus on command parsing, error handling, and output formatting
- Pre-commit hooks ensure code quality before commits

## Important Notes

1. This is a PRD/design phase project - no implementation exists yet
2. Target users are primarily AI agents requiring stable, predictable interfaces
3. All outputs should be JSON-formatted when `--output json` is specified
4. Access token management is automatic with caching and refresh
5. Interactive config wizard available via `wcli config init --interactive`
6. Pre-commit hooks enforce code formatting and quality standards