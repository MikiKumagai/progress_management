import pandas as pd
from models import task_model, progress_model
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def create_progress_chart(task_id):
    raw_data = progress_model.select_progresses_for_chart(task_id)
    task_name, total_count = task_model.select_task_for_chart(task_id)
    df = pd.DataFrame(raw_data, columns=["task_name", "task_id", "progress_value", "progress_date"])
    # TODO: Total取得して残数のグラフにする t.nameもタスクテーブルから取得する
    # TODO: 今日までの横軸にする
    df = df[df["task_name"] == task_name].copy()
    df["task_name"] = pd.to_datetime(df["progress_date"])
    df = df.sort_values("progress_date")
    df["cumulative_progress"] = df["progress_value"].cumsum()

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(df["progress_date"], df["cumulative_progress"], marker="o")
    return fig
