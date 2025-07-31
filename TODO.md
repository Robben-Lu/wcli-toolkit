# wcli 开发待办事项列表

## 🚀 项目初始化（已完成）
- [x] 创建项目目录结构
- [x] 创建必要的配置文件
- [x] 初始化Git仓库
- [x] 创建GitHub仓库并推送

## 📦 环境设置
- [ ] 安装Poetry：`curl -sSL https://install.python-poetry.org | python3 -`
- [ ] 安装项目依赖：`poetry install`
- [ ] 安装pre-commit hooks：`poetry run pre-commit install`

## 🏗️ 核心功能开发

### 1. 基础模块实现
- [ ] **wcli/core/response.py** - 实现统一响应格式
- [ ] **wcli/core/logger.py** - 配置日志系统
- [ ] **wcli/core/security.py** - 实现keyring集成
- [ ] **wcli/utils/retry.py** - 实现重试装饰器

### 2. 配置管理
- [ ] **wcli/config.py** - 实现配置文件加载
- [ ] **wcli/commands/config.py** - 实现配置命令
  - [ ] `wcli config init` - 基础初始化
  - [ ] `wcli config init --interactive` - 交互式配置向导

### 3. WeCom客户端
- [ ] **wcli/core/client.py** - 封装wechatpy客户端
  - [ ] Token管理和自动刷新
  - [ ] 错误处理和重试机制

### 4. 命令实现

#### 通讯录管理
- [ ] **wcli/commands/user.py**
  - [ ] `wcli user get --userid` - 获取用户信息
  - [ ] `wcli user list --department-id` - 列出部门成员
- [ ] **wcli/commands/department.py**
  - [ ] `wcli department list` - 获取部门列表

#### 消息管理
- [ ] **wcli/commands/msg.py**
  - [ ] `wcli msg send --to-user --text` - 发送文本消息
  - [ ] `wcli msg send-markdown --to-party --content` - 发送Markdown消息

#### 群聊管理
- [ ] **wcli/commands/group.py**
  - [ ] `wcli group create` - 创建群聊
  - [ ] `wcli group update` - 更新群聊成员

### 5. 输出格式
- [ ] 实现JSON输出格式化
- [ ] 实现表格输出（使用rich）
- [ ] 实现纯文本输出

## 🧪 测试
- [ ] 编写单元测试框架
- [ ] 为每个命令编写测试用例
- [ ] 模拟WeCom API响应
- [ ] 测试错误处理场景

## 📚 文档
- [ ] 完善README.md使用示例
- [ ] 添加API文档
- [ ] 创建贡献指南（CONTRIBUTING.md）
- [ ] 添加更改日志（CHANGELOG.md）

## 🔧 DevOps
- [ ] 配置GitHub Actions CI/CD
- [ ] 自动运行测试
- [ ] 自动检查代码格式
- [ ] 配置自动发布到PyPI

## 🎯 未来功能（V1.1+）
- [ ] 支持更多WeCom API
- [ ] 添加批量操作功能
- [ ] 实现并发请求优化
- [ ] 添加缓存机制
- [ ] 支持配置文件导入/导出

## 📝 注意事项
1. 始终遵循AI友好的设计原则
2. 保持代码模块化和可测试性
3. 重视安全性，敏感信息不能泄露
4. 确保错误信息清晰有助于调试