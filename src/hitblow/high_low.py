# src/hitblow/high_low.py

def print_high_low_hint(guess: str, secret: str, digits: int):
    """入力された予想が、正解の数字より大きいか小さいかを判定して表示する"""
    # 入力が正しい形式（数字かつ指定の桁数）の場合のみヒントを出す
    if len(guess) == digits and guess.isdigit():
        guess_num = int(guess)
        secret_num = int(secret)
        
        if guess_num < secret_num:
            print("💡 【ヒント】予想した数字は、正解より【 小さい 】です。")
        elif guess_num > secret_num:
            print("💡 【ヒント】予想した数字は、正解より【 大きい 】です。")