import pandas as pd
from models import wordbook_entry_model

def get_dictionary(task_id):
    raw_data = wordbook_entry_model.select_done_wordbook_entries(task_id)
    df = pd.DataFrame(raw_data, columns=["word", "meaning"])
    return df

def get_wordbook(task_id):
    raw_data = wordbook_entry_model.select_all_wordbook_entries(task_id)
    df = pd.DataFrame(raw_data, columns=["word", "meaning", "is_word_learned", "is_meaning_learned"])
    return df