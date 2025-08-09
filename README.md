# complexity_checklist
複雑性を見落とさないためのチェックリスト生成ツール。

## MCP Client Configuration

```json
{
  "cognitive-checklist-server": {
    "autoApprove": [
      "create_task_checklist"
    ],
    "disabled": false,
    "timeout": 60,
    "type": "stdio",
    "command": "python",
    "args": [
      "cognitive_checklist_server/server.py"
    ],
    "alwaysAllow": [
      "create_task_checklist"
    ]
  }
}
