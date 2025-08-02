import pandas as pd
from models import task_model

def get_task_progress():
    raw_data = task_model.select_task_progress()
    df = pd.DataFrame(raw_data, columns=["name", "progress", "total_count", "active"])
    return df