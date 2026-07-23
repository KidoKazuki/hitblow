"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====

    from .random_digits import randomize_game    # ← ★random_digits追加
    digits, secret = randomize_game()            # ← ★random_digits追加

    from .vs_cpu import setup_vs_cpu             # ← ★対戦モード追加
    setup_vs_cpu(digits)                         # ← ★対戦モード追加

    from .turn_limit import print_start_message  # ← ★追加
    print_start_message()                        # ← ★追加

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        from .turn_limit import process_turn         # ← ★追加
        if not process_turn(tries, secret):          # ← ★追加
            break                                    # ← ★追加

        from .high_low import print_high_low_hint    # ← ★high_low追加
        print_high_low_hint(guess, secret, digits)   # ← ★high_low追加

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)    
        print(f"  Hit={hit}  Blow={blow}")
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            print("🎉 あなたの勝利です！")        # ← ★対戦モード追加
            break

        # ユーザーが外れたら、CPUのターン！
        from .vs_cpu import play_cpu_turn        # ← ★対戦モード追加
        if play_cpu_turn(digits, secret):        # ← ★対戦モード追加
            break                                # ← ★対戦モード追加
