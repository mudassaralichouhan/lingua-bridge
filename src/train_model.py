import joblib
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from data_loader import load_dataset

def train_model(english_texts, urdu_texts):
    print("Vectorizing English texts...")
    
    vectorizer = CountVectorizer(max_features=5000)
    X = vectorizer.fit_transform(english_texts)
    y = np.array(urdu_texts)

    print(f"Feature matrix shape: {X.shape}")
    
    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Standardizing the data...")
    scaler = StandardScaler(with_mean=False)
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Training logistic regression model...")
    model = LogisticRegression(max_iter=1000, solver='liblinear')
    model.fit(X_train, y_train)

    print("Saving trained model to file...")
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '../models')
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    joblib.dump(model, os.path.join(data_dir, 'logistic_regression_model.joblib'))
    joblib.dump(vectorizer, os.path.join(data_dir, 'vectorizer.joblib'))
    print("Model trained successfully!")

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '../data')
    file_path = os.path.join(data_dir, 'parallel-corpus.xlsx')

    english_texts, urdu_texts = load_dataset(file_path)
    train_model(english_texts, urdu_texts)