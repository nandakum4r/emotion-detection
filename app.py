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

@st.cache_resource
def load_glove():
    glove_path = "embeddings/glove.6B.300d.txt"
    glove = {}
    with open(glove_path, 'r', encoding='utf8') as f:
        for line in f:
            values = line.strip().split()
            word = values[0]
            vector = np.array(values[1:], dtype=np.float32)
            glove[word] = vector
    return glove

@st.cache_resource
def load_model():
    clf = joblib.load("models/logreg_model.pkl")
    le = joblib.load("models/label_encoder.pkl")
    return clf, le

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
