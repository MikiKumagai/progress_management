import pandas as pd
from models import wordbook_entry_model

def get_wordbook_summary(wordbook_id):
    raw_data = wordbook_entry_model.fetch_all_wordbook_entry(wordbook_id)
    df = pd.DataFrame(raw_data, columns=["word", "meaning"])
    return df