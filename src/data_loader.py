import os
import pandas as pd

def load_dataset(file_path, nrows=None):
    print("Loading data...")
    df = pd.read_excel(file_path, nrows=nrows)
    
    print("Preprocessing data...")
    df.columns = df.columns.str.strip()

    english_texts = df['SENTENCES'].astype(str).tolist()
    urdu_texts = df['MEANING'].astype(str).tolist()

    if len(english_texts) != len(urdu_texts):
        raise ValueError("Length mismatch between English and Urdu texts")
    
    return english_texts, urdu_texts

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '../data')
    file_path = os.path.join(data_dir, 'parallel-corpus.xlsx')

    english_texts, urdu_texts = load_dataset(file_path, 5000)
    print("Dataset loaded successfully!")