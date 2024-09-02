# LinguaBridge

## English-to-Urdu Translation Model using Logistic Regression

### Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

### Introduction
LinguaBridge is a machine learning-based English-to-Urdu translation model designed to bridge the language gap between the two languages. Built using logistic regression, this project aims to provide accurate and efficient translations for individuals and organizations seeking to communicate across linguistic and cultural boundaries.

### Installation
To install the LinguaBridge project, follow these steps:

**Clone the Repository**
   ```bash
   git clone https://github.com/mudassaralichouhan/lingua-bridge.git
   ```

**Install Dependencies**
   ```bash
   pip install virtualenv
   cd lingua-bridge/
   python -m venv env
   source env/bin/activate
   echo $VIRTUAL_ENV
   pip install -r requirements.txt
   ```

### Usage
1. Load the dataset: `python3.12 src/data_loader.py`
```bash
$ python3.12 src/data_loader.py
Loading data...
Preprocessing data...
Dataset loaded successfully!
```
2. Train the model: `python3.12 src/train_model.py`
```bash
$ python3.12 src/train_model.py 
Loading data...
Preprocessing data...
Vectorizing English texts...
Splitting data into training and testing sets...
Training logistic regression model...
Saving trained model to file...
Model trained successfully!
```
3. Evaluate the model: `python3.12 src/evaluate_model.py`
```bash
$ python3.12 src/evaluate_model.py
Loading data...
Preprocessing data...
Loading pre-trained model...
Evaluating model accuracy...
Model accuracy: 10.82%
Model evaluation completed successfully!
```
4. Use the model for translation: `python3.12 src/translate.py`
```python
translate(["Hello, how are you?"])
```
```bash
$ python3.12 src/translate.py 
Loading pre-trained model...
Making prediction on new sentence...
Printing predicted translation...
Predicted translation: آپ کیسے ہو؟
Translation completed successfully!
```

### Contributing
Contributions are welcome! If you'd like to contribute to the LinguaBridge project, please fork the repository and submit a pull request.

### License
LinguaBridge is licensed under the MIT License.

### requirements.txt
Here's a sample `requirements.txt` file:
```python
pandas==2.2.2
datasets==2.21.0
scikit-learn==1.5.1
openpyxl==3.1.5
joblib==1.4.2
````

### External Resources:
   - [English-Urdu Parallel Corpus](https://www.kaggle.com/datasets/muhammadanasmahmood/englishurdu-parallel-corpus)
   - [Demo](https://colab.research.google.com/drive/1wo0FfV2Cd6wI3v3JuhvkyASBy38OUfwa?usp=sharing)
   - [Demo 2](https://colab.research.google.com/drive/1w5c9OW1Q_IdEj6K22mk9gv_Z9KDKUAqV?usp=sharing)