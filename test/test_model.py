import joblib
import pandas as pd
from datasets import Dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    file_path = '../data/parallel-corpus.xlsx'
    df = pd.read_excel(file_path)

    df.columns = df.columns.str.strip()
    english_texts = df['SENTENCES'].astype(str).tolist()
    urdu_texts = df['MEANING'].astype(str).tolist()

    data = {
        'en': english_texts,
        'ur': urdu_texts,
    }
    dataset = Dataset.from_dict(data)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(english_texts)
    y = urdu_texts

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)


    joblib.dump(model, '../models/logistic_regression_model.joblib')