# app.py
import streamlit as st
import numpy as np
import re
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Load GloVe .pkl once
@st.cache_resource
def load_glove():
    return joblib.load("embeddings/glove.6B.300d.pkl")

# Load saved model and label encoder
@st.cache_resource
def load_model():
    clf = joblib.load("model/logreg_model.pkl")
    le = joblib.load("model/label_encoder.pkl")
    return clf, le

# Text preprocessing
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text.lower())
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]

# Get vector representation
def get_sentence_vector(tokens, glove, dim=300):
    vectors = [glove[word] for word in tokens if word in glove]
    return np.mean(vectors, axis=0) if vectors else np.zeros(dim)

# UI
st.title("🧠 Emotion Detection App")
text_input = st.text_input("Enter a sentence:")

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        glove = load_glove()
        clf, le = load_model()
        tokens = preprocess_text(text_input)
        vector = get_sentence_vector(tokens, glove)
        prediction = clf.predict([vector])[0]
        emotion = le.inverse_transform([prediction])[0]
        st.success(f"Predicted Emotion: **{emotion}**")
