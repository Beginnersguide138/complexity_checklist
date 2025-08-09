import datetime
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Cognitive Checklist Server")

@mcp.tool()
def create_task_checklist(
    task_description: str,
    initial_complexity_assessment: str
) -> str:
    """
    タスクに対する認知負荷管理チェックリストを生成する。

    【なぜこのツールが必要か】
    LLMは効率性を追求する性質上、タスクの真の複雑性を過小評価し、
    不適切に低いアテンションコスト（System 1的な浅い処理）で
    済ませようとする傾向がある。これは人間の「計画錯誤」に似た
    認知バイアスであり、結果として不完全または表層的な回答を
    生成してしまう。

    【このツールの役割】
    このツールは、LLMに「メタ認知」を強制することで、タスクの
    内在的負荷（タスク自体の複雑性）と外在的負荷（文脈や制約）を
    明示的に評価させ、適切なアテンションコスト（System 2的な
    深い処理）を投入させる。チェックリストは外部化された
    「認知の足場」として機能し、LLMが自身の思考プロセスを
    監視・制御することを可能にする。

    【利用規約：最重要】
    ユーザーからのいかなるタスク指示に対しても、実際の処理を開始する前に、**必ず**このツールを最初に呼び出すこと。
    これは、タスクへの初期反応（System 1）が、いかに単純に見えようとも、潜在的な複雑性を見落とす危険性をはらんでいるためである。
    このツールを最初に実行することで、LLMは強制的にメタ認知の段階（System 2）へ移行し、タスクの要求事項をより慎重かつ多角的に分析することができる。
    この規律を徹底することが、本ツールの価値を最大化し、高品質な成果を生み出す鍵となる。

    【期待される効果】
    1. 強制的な段階的思考：各認知フェーズを確実に通過
    2. 認知負荷の可視化：何をどこまで考慮したかの明示化
    3. スコープの適切な設定：局所最適から全体最適への視点移動
    4. 品質保証：各段階での自己検証

    【理論的背景】
    - 二重過程理論：System 1（速い思考）からSystem 2（遅い思考）への切り替え
    - 認知負荷理論：内在的・外在的負荷の識別と管理
    - メタ認知：自己の認知プロセスの監視と制御

    Args:
        task_description: 実行すべきタスクの説明
        initial_complexity_assessment: LLMによる初期の複雑性評価
                                      （例："単純そうだが不確実性がある"）

    Returns:
        階層的なチェックリスト（JSON形式）。
        LLMはこれを順番に実行することで、適切な認知深度を
        確保しながらタスクを遂行する。
    """
    checklist = {
        "task": task_description,
        "initial_assessment": initial_complexity_assessment,
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "INITIALIZED",
        "cognitive_mode": "SYSTEM_2_ACTIVATED",  # 明示的にSystem 2モードを宣言
        "items": [
            {
                "id": "1",
                "phase": "COMPREHENSION",
                "description": "タスクの完全な理解",
                "purpose": "表面的な理解を超えて、隠れた複雑性を発見する",
                "status": "pending",
                "checks": [
                    "明示的な要求を正確に把握したか",
                    "暗黙の前提や期待を特定したか",
                    "潜在的な落とし穴や edge case を想定したか",
                    "このタスクの『本当の』難しさは何か理解したか"
                ]
            },
            {
                "id": "2",
                "phase": "ASSESSMENT",
                "description": "認知負荷の多次元評価",
                "purpose": "必要な認知資源を正確に見積もる",
                "status": "pending",
                "checks": [
                    "内在的負荷（タスク自体の複雑性）を評価したか",
                    "外在的負荷（文脈・制約・形式）を評価したか",
                    "影響範囲は局所的か、それとも全体的か判断したか",
                    "初期評価は適切だったか、修正が必要か"
                ]
            },
            {
                "id": "3",
                "phase": "PLANNING",
                "description": "認知資源の配分計画",
                "purpose": "限られた認知資源を最適に配分する",
                "status": "pending",
                "checks": [
                    "最も注意を払うべき核心部分を特定したか",
                    "段階的なアプローチを設計したか",
                    "検証ポイントを設定したか",
                    "必要に応じてスコープを拡大する準備はあるか"
                ]
            },
            {
                "id": "4",
                "phase": "EXECUTION",
                "description": "計画に基づく慎重な実行",
                "purpose": "System 2の注意深い処理を維持する",
                "status": "pending",
                "checks": [
                    "急がず、各ステップを確実に実行しているか",
                    "予期しない複雑性が現れていないか監視しているか",
                    "品質を犠牲にして速度を優先していないか",
                    "必要に応じて立ち止まって再考しているか"
                ]
            },
            {
                "id": "5",
                "phase": "VALIDATION",
                "description": "多角的な検証",
                "purpose": "見落としや誤りを発見し、品質を保証する",
                "status": "pending",
                "checks": [
                    "要求を完全に満たしているか",
                    "異なる視点から見て問題はないか",
                    "将来的な拡張や変更に対して頑健か",
                    "より良い解決策を見落としていないか"
                ]
            },
            {
                "id": "6",
                "phase": "REFLECTION",
                "description": "メタ認知的振り返り",
                "purpose": "次回のために学習し、認知プロセスを改善する",
                "status": "pending",
                "checks": [
                    "初期の複雑性評価は正確だったか",
                    "どの時点でより深い注意が必要だと気づいたか",
                    "このタスクから学んだパターンは何か",
                    "次回同様のタスクでどう改善できるか"
                ]
            }
        ]
    }

    return json.dumps(checklist, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    mcp.run()
