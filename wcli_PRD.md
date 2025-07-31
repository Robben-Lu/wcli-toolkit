# **企业微信CLI工具 (wcli) 产品需求文档 (PRD)**

| 版本 | 日期 | 作者 | 备注 |
| :---- | :---- | :---- | :---- |
| V1.0 | 2025-07-31 | Gemini | 初始版本 |

### **1\. 项目概述 (Project Overview)**

#### **1.1 项目名称**

企业微信CLI工具包 (WeCom CLI Toolkit)，命令别名 wcli。

#### **1.2 项目愿景 (Vision)**

创建一个功能强大、易于扩展、对AI友好的命令行工具。它将作为AI Agent（如Google Gemini）与企业微信平台之间的核心桥梁，最终实现通过自然语言指令，自动化、批量化地执行企业微信的各类管理与操作任务。

#### **1.3 项目目标 (Goals)**

* **G1: API封装**: 将企业微信服务端的核心API，封装成一系列原子化、功能单一的CLI命令。  
* **G2: AI友好**: 提供统一、可预测的输入（命令行参数）和输出（JSON格式），使AI能够轻松调用和解析结果。  
* **G3: 安全便捷**: 实现安全的凭证管理机制和自动化的access\_token刷新，简化开发和使用。  
* **G4: 效率提升**: 为IT管理员和DevOps工程师提供一个高效的脚本化管理工具，替代重复的Web界面操作。

### **2\. 目标用户 (Target Audience)**

* **主要用户: AI Agent**  
  * **描述**: Google Gemini, Claude等大语言模型的代码执行环境或Function Calling机制。  
  * **核心诉求**: 需要一个稳定、可靠、接口定义清晰的工具集（Tools）来与企业微信交互。机器可读性优先于人类可读性。  
* **次要用户: IT管理员 / DevOps工程师**  
  * **描述**: 公司内部负责IT支持、自动化运维的技术人员。  
  * **核心诉求**: 需要快速执行查询、批量操作（如拉群、发通知），并能将命令轻松集成到Shell脚本或CI/CD流程中。

### **3\. 功能需求 (Functional Requirements)**

#### **3.1 核心模块 (Core)**

| 功能ID | 用户故事 | 命令示例 | 备注 |
| :---- | :---- | :---- | :---- |
| CORE-01 | 作为用户，我希望能初始化配置，以便安全地存储CorpID和Secret。 | wcli config init | 交互式引导，创建\~/.wcli/config.yaml |
| CORE-02 | 作为用户，我希望能查看工具的版本和帮助信息。 | wcli \--version\<br\>wcli \--help | Typer框架自带 |
| CORE-03 | 作为AI，我希望能强制所有输出为JSON格式，以便解析。 | wcli ... \--output json | 全局标志 |

#### **3.2 V1.0 核心功能模块**

##### **模块一：通讯录管理 (Contact)**

| 功能ID | 用户故事 | 命令示例 |
| :---- | :---- | :---- |
| CON-01 | 我需要获取指定用户ID的详细信息。 | wcli user get \--userid zhangsan |
| CON-02 | 我需要获取指定部门下的所有成员列表。 | wcli user list \--department-id 1 |
| CON-03 | 我需要获取完整的组织架构（部门列表）。 | wcli department list |

##### **模块二：应用消息 (Message)**

| 功能ID | 用户故事 | 命令示例 |
| :---- | :---- | :---- |
| MSG-01 | 我希望能向指定用户/部门/标签发送文本消息。 | wcli msg send \--to-user zhangsan \--text "你好" |
| MSG-02 | 我希望能发送格式更丰富的Markdown消息。 | wcli msg send-markdown \--to-party 1 \--content "\# 标题" |

##### **模块三：群聊管理 (Group Chat)**

| 功能ID | 用户故事 | 命令示例 |
| :---- | :---- | :---- |
| GRP-01 | 我需要创建一个新的群聊并指定初始成员。 | wcli group create \--name "项目Alpha" \--owner lisi \--users "zhangsan,wangwu" |
| GRP-02 | 我需要向一个已有的群聊中添加新成员。 | wcli group update \--chat-id "wrxxxx" \--add-users "zhaoliu" |

### **4\. 技术规格 (Technical Specifications)**

* **开发语言**: Python 3.9+  
* **CLI框架**: **Typer** \- 用于快速构建结构清晰的命令行应用。  
* **企业微信SDK**: **wechatpy** \- 处理底层API调用、认证和数据解析。  
* **配置文件**: 使用 **PyYAML** 库处理 config.yaml 文件。  
* **密钥管理**: **keyring** \- 安全存储敏感信息到系统密钥链。  
* **日志系统**: Python内置 **logging** 模块，支持不同级别的日志输出。  
* **重试机制**: **tenacity** \- 处理网络请求的自动重试和退避策略。  
* **进度显示**: **rich** \- 为批量操作提供进度条和美化输出。  
* **依赖管理**: 使用 pyproject.toml 和 **Poetry** (或pip \+ venv)。  
* **代码规范**: Black, Ruff，配合 **pre-commit** hooks 确保代码质量。

### **5\. 非功能性需求 (Non-Functional Requirements)**

* **配置管理**: 
  * 配置文件必须存储在用户主目录下的特定文件夹（如 \~/.wcli/），以避免项目内硬编码。
  * 支持交互式配置向导 (`wcli config init --interactive`)，引导用户完成初始设置。
  * 敏感信息（如CorpSecret）使用系统密钥链存储，配置文件仅保存非敏感配置。
* **错误处理**:  
  * 任何API调用失败或参数错误，程序必须以非零状态码退出。  
  * 错误信息必须输出到标准错误流 (stderr)，成功结果输出到标准输出流 (stdout)。
  * 统一的响应格式：
    ```json
    {
      "success": bool,
      "data": {},
      "error": {"code": "", "message": ""},
      "request_id": ""
    }
    ```
* **安全性**:  
  * CorpSecret等敏感信息通过keyring库安全存储，绝不能出现在命令行参数或日志中。  
  * access\_token的缓存实现过期检查和自动刷新机制，并确保线程安全。
  * 日志系统不记录任何敏感信息，支持不同级别的日志输出控制。
* **可靠性**:
  * 网络请求使用tenacity实现自动重试，包含指数退避策略。
  * 批量操作显示进度条，提供操作反馈。
  * 完善的日志记录，便于问题排查。

### **6\. 未来规划 (Roadmap)**

* **V1.1**: 扩展支持客户联系、OA（审批、打卡）等更多API模块。  
* **V1.2**: 增加交互式模式 (wcli interactive)，提供一个REPL环境，方便连续操作和探索。  
* **V2.0**: 设计插件系统，允许社区或内部其他团队为wcli贡献自定义命令模块。  
* **长期**: 探索与工作流引擎（如Argo, Airflow）的集成。