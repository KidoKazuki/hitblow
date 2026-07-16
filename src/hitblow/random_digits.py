# src/hitblow/random_digits.py
import random
from .core import make_secret


def randomize_game() -> tuple[int, str]:
    """3〜5のランダムな桁数を決定し、新しい桁数と秘密の数字を生成して返す"""
    digits = random.randint(3, 5)
    secret = make_secret(digits)
    
    print(f"🎲 【難易度ランダム】今回は【 {digits} 桁 】で勝負です！")
    return digits, secret