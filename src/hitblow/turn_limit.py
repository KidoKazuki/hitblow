# src/hitblow/turn_limit.py

MAX_TURNS = 10  # 制限ターン数


def print_start_message():
    """ゲーム開始時のメッセージを表示する"""
    print(f"※ 制限ターン数: {MAX_TURNS}回")


def process_turn(tries: int, secret: str) -> bool:
    """ターン制限のチェックと残りターンの表示を行う。

    ゲームを継続する場合は True、ゲームオーバーの場合は False を返す。
    """
    # すでに制限回数に達している場合
    if tries >= MAX_TURNS:
        print(f"ゲームオーバー！制限ターン数（{MAX_TURNS}回）に達しました。")
        print(f"正解は {secret} でした。")
        return False

    # 残りターン数を表示して継続
    remaining = MAX_TURNS - tries
    print(f"【残りターン数: {remaining} / {MAX_TURNS}】")
    return True