# src/hitblow/vs_cpu.py
import random
from itertools import permutations
from .core import judge

_player_secret = ""
_candidates = []


def setup_vs_cpu(digits: int):
    """ユーザーにCPUに当てさせる自分の数字を入力してもらう"""
    global _player_secret, _candidates
    print(f"\n⚔️ 【対戦モード】CPUもあなたも【 {digits} 桁 】で勝負します！")

    while True:
        val = input(f"CPUに当てさせるあなたの数字（{digits}桁・重複なし）を入力 > ").strip()
        if len(val) == digits and val.isdigit() and len(set(val)) == digits:
            _player_secret = val
            print(f"👉 あなたの数字を「{val}（{digits}桁）」に設定しました。勝負開始！\n")
            break
        print(f"※ 重複のない {digits} 桁の数字を入力してください。")

    # CPUの予想候補（全パターンの数字）を用意する
    all_digits = [str(i) for i in range(10)]
    _candidates = ["".join(p) for p in permutations(all_digits, digits)]


def play_cpu_turn(digits: int, secret: str = "") -> bool:
    """CPUがプレイヤーの数字を予想する。CPUが正解したら True を返す"""
    global _candidates

    if not _candidates:
        cpu_guess = "".join(random.sample("0123456789", digits))
    else:
        cpu_guess = random.choice(_candidates)

    hit, blow = judge(_player_secret, cpu_guess)
    print(f"🤖 CPUの予想 > {cpu_guess}  (Hit={hit}, Blow={blow})")

    if hit == digits:
        print(f"\n💥 残念！CPUがあなたの数字（{_player_secret}）を先に当てました！CPUの勝ち！")
        if secret:
            print(f"📢 ちなみにCPUの数字（あなたが当てるはずだった答え）は「{secret}」でした！")
        return True

    # Hit/Blowの結果から、可能性のない数字をCPUの候補から除外（絞り込み）
    _candidates = [c for c in _candidates if judge(c, cpu_guess) == (hit, blow)]
    return False