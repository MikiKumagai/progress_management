import pandas as pd
from models import task_model

def get_task_summary():
    raw_data = task_model.fetch_all_tasks()
    df = pd.DataFrame(raw_data, columns=["name", "progress", "total_count", "active"])
    return df