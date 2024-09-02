import joblib
import os
from sklearn.model_selection import train_test_split
from data_loader import load_dataset

def evaluate_model(english_texts, urdu_texts):
    print("Loading pre-trained model...")
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '../models')

    loaded_model = joblib.load(os.path.join(data_dir, 'logistic_regression_model.joblib'))
    loaded_vectorizer = joblib.load(os.path.join(data_dir, 'vectorizer.joblib'))

    print("Evaluating model accuracy...")
    X = loaded_vectorizer.transform(english_texts)
    y = urdu_texts
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    score = loaded_model.score(X_test, y_test)
    print(f"Model accuracy: {score * 100:.2f}%")
    print("Model evaluation completed successfully!")

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '../data')
    file_path = os.path.join(data_dir, 'parallel-corpus.xlsx')

    english_texts, urdu_texts = load_dataset(file_path)
    evaluate_model(english_texts, urdu_texts)