# Cognitive Complexity Checklist

**LLMの「計画錯誤」を防ぎ、タスクの真の複雑性に向き合うためのメタ認知ツール**

---

## 概要

`Cognitive Complexity Checklist` は、大規模言語モデル (LLM) がタスクを実行する際に、その複雑性を過小評価してしまう認知バイアス（計画錯誤に類似）を軽減するためのツールです。

LLMは効率性を追求するあまり、本質的に複雑なタスクに対しても表層的な理解（System 1思考）で処理しようとする傾向があります。その結果、アウトプットの品質が低下したり、重要な要素が見落とされたりする問題が発生します。

このツールは、LLMに「メタ認知」のプロセスを強制するチェックリストを動的に生成します。これにより、LLMはタスクの内在的・外在的負荷を体系的に評価し、より深く慎重な思考（System 2思考）へと切り替えることを促されます。生成されたチェックリストは、LLMが自身の思考プロセスを監視・制御するための「認知的な足場」として機能します。

## 利用の基本原則

**最重要**: LLMはユーザーからタスクの指示を受けた際、実際の処理を開始する前に、**必ず**この `create_task_checklist` ツールを実行しなければなりません。

これは、タスクへの初期反応（System 1）が、いかに単純に見えようとも、潜在的な複雑性を見落とす危険性をはらんでいるためです。このツールを最初に実行することで、LLMは強制的にメタ認知の段階（System 2）へ移行し、タスクの要求事項をより慎重かつ多角的に分析することができます。この規律を徹底することが、本ツールの価値を最大化し、高品質な成果を生み出す鍵となります。

## 主な機能

- **動的なチェックリスト生成**: タスクの説明と初期の複雑性評価に基づき、認知負荷を管理するための階層的なチェックリストをJSON形式で生成します。
- **メタ認知プロセスの強制**: 「理解」「評価」「計画」「実行」「検証」「振り返り」という6つの認知フェーズを定義し、LLMが各段階を確実に経るように誘導します。
- **System 2思考への切り替え**: 複雑なタスクに対して、意図的に深く、分析的な思考をアクティベートさせ、アウトプットの品質向上を図ります。

## 技術スタック

- **サーバー**: Python 3
- **Webフレームワーク**: [FastMCP](https://github.com/model-context-protocol/fastmcp)
- **パッケージ管理**: [uv](https://github.com/astral-sh/uv)

## セットアップと実行

1.  **リポジトリをクローンします**:
    ```bash
    git clone https://github.com/your-username/complexity_checklist.git
    cd complexity_checklist
    ```

2.  **依存関係をインストールします**:
    プロジェクトルートには `cognitive_checklist_server` ディレクトリがあります。`uv` を使って、このサーバーの依存関係をインストールします。
    ```bash
    uv pip install -e cognitive_checklist_server
    ```

3.  **MCPサーバーを起動します**:
    以下のコマンドでMCPサーバーを起動します。
    ```bash
    uv run --directory cognitive_checklist_server server.py
    ```
    サーバーが起動し、MCPクライアントからの接続を待ち受けます。

## MCPクライアント設定

Kilo CodeなどのMCPクライアントからこのサーバーを利用するには、クライアントの設定ファイルに以下の構成を追加してください。

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
**注意**: `/path/to/your/complexity_checklist` の部分は、あなたの環境におけるリポジトリの絶対パスに置き換えてください。

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下で公開されています。
