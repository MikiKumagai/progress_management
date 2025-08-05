import pandas as pd
from models import task_model, progress_model, wordbook_entry_model
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
    df["progress_date"] = pd.to_datetime(df["progress_date"])
    today = pd.to_datetime(date.today())
    # 今日のデータがあるかチェック
    if not (df["progress_date"] == today).any():
        new_row = {
            "task_name": task_name,
            "task_id": task_id,
            "progress_value": 0,
            "progress_date": today,
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
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

def create_wordbook_progress_chart(task_id):
    raw_data = wordbook_entry_model.select_wordbook_progresses_for_chart(task_id)
    task_name, total_count = task_model.select_task_for_chart(task_id)
    df = pd.DataFrame(raw_data, columns=["task_name", "task_id", "word_learned_at", "meaning_learned_at"])
    df = df[df["task_name"] == task_name].copy()

    df["word_learned_at"] = pd.to_datetime(df["word_learned_at"])
    df["meaning_learned_at"] = pd.to_datetime(df["meaning_learned_at"])
    df["progress_date"] = df[["word_learned_at", "meaning_learned_at"]].max(axis=1)
    
    grouped = df.groupby(["task_name", "task_id", "progress_date"]).size().reset_index(name="progress_value")

    today = pd.to_datetime(date.today())
    if not (grouped["progress_date"] == today).any():
        new_row = {
            "task_name": task_name,
            "task_id": task_id,
            "progress_value": 0,
            "progress_date": today,
        }
        grouped = pd.concat([grouped, pd.DataFrame([new_row])], ignore_index=True)
    
    grouped = grouped.sort_values("progress_date")
    grouped["cumulative_progress"] = grouped["progress_value"].cumsum()
    grouped["remaining_value"] = total_count - grouped["cumulative_progress"]

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(grouped["progress_date"], grouped["remaining_value"])
    ax.xaxis.set_major_locator(AutoDateLocator())
    ax.set_ylim(bottom=0)
    fig.autofmt_xdate()
    return fig
