import pandas as pd
import os
from datasets import Dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

script_dir = os.path.dirname(__file__)
models_dir = os.path.join(script_dir, '../models')
data_dir = os.path.join(script_dir, '../data')

print("Initializing program...")
print("Loading data...")
file_path = '../data/parallel-corpus.xlsx'
df = pd.read_excel(file_path, nrows=5000)

print("Preprocessing data...")
df.columns = df.columns.str.strip()
english_texts = df['SENTENCES'].astype(str).tolist()
urdu_texts = df['MEANING'].astype(str).tolist()

if len(english_texts) != len(urdu_texts):
    raise ValueError("Length mismatch between English and Urdu texts")

print("Creating dataset...")
data = {
    'en': english_texts,
    'ur': urdu_texts,
}
dataset = Dataset.from_dict(data)

print("Vectorizing English texts...")
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(english_texts)
y = urdu_texts

print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training logistic regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Evaluating model accuracy...")
score = model.score(X_test, y_test)
print(f"Model accuracy: {score * 100:.2f}%")

print("Making prediction on new sentence...")
new_sentence = ["Hello, how are you?"]
new_sentence_vectorized = vectorizer.transform(new_sentence)
prediction = model.predict(new_sentence_vectorized)

print("Printing predicted translation...")
print(f"Predicted translation: {prediction[0]}")

print("Program completed successfully!")