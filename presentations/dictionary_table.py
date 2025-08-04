import pandas as pd
from models import wordbook_entry_model

def get_wordbook_summary(task_id):
    raw_data = wordbook_entry_model.fetch_all_wordbook_entries(task_id)
    df = pd.DataFrame(raw_data, columns=["word", "meaning"])
    return df