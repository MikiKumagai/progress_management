import pandas as pd
from models import task_model, progress_model
import matplotlib.pyplot as plt
from datetime import date
from matplotlib.figure import Figure
from matplotlib.dates import DayLocator, AutoDateLocator

def create_progress_chart(task_id):
    # データ取得
    raw_data = progress_model.select_progresses_for_chart(task_id)
    task_name, total_count = task_model.select_task_for_chart(task_id)
    # 必要な情報を整える
    df = pd.DataFrame(raw_data, columns=["task_name", "task_id", "progress_value", "progress_date"])
    df = df[df["task_name"] == task_name].copy()
    df["progress_date"] = pd.to_datetime(df["progress_date"])
    # 今日の日付までにフィルタ
    today = pd.to_datetime(date.today())
    df = df[df["progress_date"] <= today]
    # 累積を計算
    df = df.sort_values("progress_date")
    df["cumulative_progress"] = df["progress_value"].cumsum()
    df["remaining_value"] = total_count - df["cumulative_progress"]

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(df["progress_date"], df["remaining_value"])
    ax.xaxis.set_major_locator(AutoDateLocator())
    ax.set_ylim(bottom=0)
    fig.autofmt_xdate()
    return fig
