"""
記憶の定着率を計算するロジックモジュール。
エビングハウスの忘却曲線モデルを使用する。
"""

import math
def calculate_retention(time, stability):
    """
    エビングの忘却曲線の数式を再現する関数
    """
    # ここに計算式を書く
    retention = math.exp(-time / stability)
    return retention

def update_storage(current_stability, is_correct: bool):
    """
    記憶の保存量を更新する関数
    """
    if is_correct:
        return current_stability *2
    else:
        return max(1, current_stability / 2)
    
    Python

def predict_next_review(stability, target_retention=0.5):
    """
    記憶が target_retention (例: 0.5 = 50%) まで落ちる時間を予測する
    数式: t = -S * ln(R)
    """
    # math.log は自然対数(ln)です
    time_left = -stability * math.log(target_retention)
    return round(time_left)
# テスト用
# --- シミュレーション開始 ---
# テスト: 強度(s)が 50 の時、記憶が半分(0.5)になるのは何分後？
s = 50
minutes = predict_next_review(s, 0.5)
print(f"現在の強度{s}だと、あと {minutes} 分で忘れます。復習してください！")

# 復習して強度が100になったら？
s = update_storage(s, True) # 100になる
minutes = predict_next_review(s, 0.5)
print(f"レベルアップ！次は {minutes} 分後まで忘れません。")