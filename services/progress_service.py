from models import task_model, progress_model

# 進捗記録ページ：進捗記録
def add_progress(task_id, progress_value, progress_type):
    progress, total_count = task_model.select_task_data(task_id)
    progress_total, progress_diff = calculate_progress(progress, progress_value, progress_type)
    # 進捗を登録
    if progress_model.select_today_data(task_id) is None:
        progress_model.insert_progress(task_id, progress_diff)
    else:
        progress_model.update_progress(task_id, progress_diff)
    # taskの進捗情報を更新
    task_model.update_task_progress(task_id, progress_total)
    # task完了しているかチェック
    if progress_total == total_count:
        task_model.update_task_completion(task_id)

# 進捗記録ページ：進捗記録データの計算
def calculate_progress(progress, progress_value, progress_type):
    if progress_type == "累計":
        progress_total = progress_value
        progress_diff = progress_value - progress
    elif progress_type == "差分":
        progress_total = progress_value + progress
        progress_diff = progress_value
    else:
        raise ValueError("不明な入力タイプ")
    return progress_total, progress_diff

# 進捗記録ページ：進捗率を算出
import math
def get_rate(task_id):
    progress, total_count = task_model.select_task_data(task_id)
    rate = progress / total_count
    return rate * 100 

# 進捗記録ページ：完了日をLinearRegressionで予測
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import timedelta
from datetime import date
import numpy as np
def get_predict(task_id):
    # 進捗データを取得
    raw_progress = progress_model.select_progresses_for_predict(task_id)
    if not raw_progress:
        return None
    df = pd.DataFrame(raw_progress, columns=["progress_date", "progress_value"])

    # TODO: 進捗率100パーだったらmaxの日を返す

    # X：学習開始からの日数
    dates = pd.to_datetime(df["progress_date"])
    start = dates.iloc[0]
    X = (dates - start).dt.days.to_numpy().reshape(-1, 1)  

    # y：累積進捗率（%）
    cumulative_sums = df["progress_value"].cumsum()
    # TODO: progress_modelで一緒に取ってくる
    total = task_model.select_task_for_predict(task_id)[0]
    y = (cumulative_sums / total * 100).to_numpy()

    model = LinearRegression()
    model.fit(X, y)
    a = model.coef_[0]
    b = model.intercept_

    # TODO: 最終更新〜今日の空白期間しか考慮できてないので要検討
    finish_day = (100 - b) / a
    finish_date = start + timedelta(days=round(finish_day))
    blank_period = date.today() - dates.max().date()
    return finish_date + blank_period

