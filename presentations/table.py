import pandas as pd
from models import progress_model

# TODO: ProgressOverviewPageで表示
def get_progress_summary():
    raw_data = progress_model.fetch_all_progresses()
    df = pd.DataFrame(raw_data, columns=["task_name", "progress_value", "progress_date"])
    return df