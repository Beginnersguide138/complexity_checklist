[English](README.md) | [日本語](README.ja.md)

---
# 认知复杂性清单

**一个元认知工具，旨在防止LLM的“规划谬误”并正视任务的真实复杂性**

---

## 概述

`认知复杂性清单` 是一个旨在减轻大语言模型（LLM）低估任务复杂性的认知偏见（类似于人类的“规划谬误”）的工具。

为了追求效率，LLM倾向于用表面的理解（系统1思维）来处理本质上复杂的任务。这可能导致输出质量下降和关键要素被忽略。

该工具动态生成一个清单，强制LLM进行“元认知”过程。它促使LLM系统地评估任务的内在和外在认知负荷，鼓励向更深入、更审慎的思考（系统2思维）转变。生成的清单作为“认知脚手架”，使LLM能够监控和调节其自身的思维过程。

## 核心使用原则

**至关重要**：当LLM从用户那里接收到任务指令时，它**必须**在开始实际处理之前执行 `create_task_checklist` 工具。

这是因为对任务的初步反应（系统1），无论看起来多么简单，都存在忽略潜在复杂性的风险。首先运行此工具会强制LLM进入元认知阶段（系统2），从而可以对任务需求进行更仔细、更多方面的分析。遵守这一纪律是最大化该工具价值并产生高质量成果的关键。

### 清单追踪的最佳实践

LLM在生成清单后“忘记”它是一个常见的挑战。为了解决这个问题，建立一个工作流程，让LLM扮演一个勤勉的项目经理至关重要。`update_todo_list` 工具在此过程中是必不可少的。

**推荐工作流程：**

1.  **分配角色**：在任务开始时，明确指示LLM：
    > “你是一个任务管理器。你的职责是使用 `update_todo_list` 工具将 `create_task_checklist` 生成的项目注册到TODO列表中，并一丝不苟地跟踪和更新每个项目的进度。”

2.  **初始化清单**：在 `create_task_checklist` 生成列表后，立即使用 `update_todo_list` 工具注册所有项目。将第一个项目标记为“进行中 `[-]`”。

    **`update_todo_list` 调用示例：**
    ```xml
    <update_todo_list>
    <todos>
    [-] 阶段一：理解
    [ ] 阶段二：评估
    [ ] 阶段三：规划
    [ ] 阶段四：执行
    [ ] 阶段五：验证
    [ ] 阶段六：反思
    </todos>
    </update_todo_list>
    ```

3.  **强制状态更新**：每当LLM完成一个任务项时，它**必须**再次调用 `update_todo_list` 来更新状态。将已完成的项目标记为“已完成 `[x]`”，并将下一个项目标记为“进行中 `[-]`”。

4.  **自我参照**：在每个步骤开始时，LLM应参考当前的TODO列表以确认下一步需要做什么。这就创建了一个有状态的循环，防止清单被遗忘。

通过遵循此工作流程，LLM被迫维持上下文并主动管理任务状态，将清单从一个静态的一次性产物转变为一个动态且真正有用的项目管理工具。

## 主要特点

- **动态清单生成**：根据任务描述和初步的复杂性评估，以JSON格式生成用于管理认知负荷的层级清单。
- **强制元认知过程**：定义了六个认知阶段——理解、评估、规划、执行、验证和反思——以可靠地引导LLM完成每个阶段。
- **转向系统2思维**：针对复杂任务，有意激活深入的分析性思维，以提高输出质量。

## 技术栈

- **服务器**：Python 3
- **Web框架**：[FastMCP](https://github.com/model-context-protocol/fastmcp)
- **包管理器**：[uv](https://github.com/astral-sh/uv)

## 设置与执行

1.  **克隆代码仓库**：
    ```bash
    git clone https://github.com/your-username/complexity_checklist.git
    cd complexity_checklist
    ```

2.  **安装依赖项**：
    项目根目录包含 `cognitive_checklist_server` 目录。使用 `uv` 来安装其依赖项。
    ```bash
    uv pip install -e cognitive_checklist_server
    ```

3.  **启动MCP服务器**：
    使用以下命令启动MCP服务器：
    ```bash
    uv run --directory cognitive_checklist_server server.py
    ```
    服务器将启动并等待来自MCP客户端的连接。

## MCP客户端配置

要从像Kilo Code这样的MCP客户端使用此服务器，请将以下配置添加到您的客户端设置文件中。

```json
{
  "cognitive-checklist-server": {
    "autoApprove": [
      "create_task_checklist"
    ],
    "disabled": false,
    "timeout": 60,
    "type": "stdio",
    "command": "uv",
    "args": [
      "run",
      "--directory",
      "/path/to/your/complexity_checklist/cognitive_checklist_server",
      "server.py"
    ],
    "alwaysAllow": [
      "create_task_checklist"
    ]
  }
}
```
**注意**：请将 `/path/to/your/complexity_checklist` 替换为您环境中代码仓库的绝对路径。

## 许可证

该项目根据 [MIT 许可证](LICENSE) 授权。