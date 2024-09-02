import joblib
import os

def translate(new_sentence):
    print("Loading pre-trained model...")
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '../models')
    loaded_model = joblib.load(os.path.join(data_dir, 'logistic_regression_model.joblib'))
    loaded_vectorizer = joblib.load(os.path.join(data_dir, 'vectorizer.joblib'))

    print("Making prediction on new sentence...")
    new_sentence_vectorized = loaded_vectorizer.transform(new_sentence)
    prediction = loaded_model.predict(new_sentence_vectorized)
    
    print("Printing predicted translation...")
    print(f"Predicted translation: {prediction[0]}")
    print("Translation completed successfully!")

if __name__ == "__main__":
    new_sentence = ["Hello, how are you?"]
    translate(new_sentence)