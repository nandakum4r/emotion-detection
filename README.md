# Emotion Detection

This project is an emotion detection system that uses natural language processing techniques to classify text into different emotions.

## Features

- Text preprocessing and cleaning
- Emotion classification using logistic regression model

## Requirements

- Python 3.7+
- Required Python packages (see `requirements.txt`)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nandakum4r/emotion-detection.git
   cd emotion-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download GloVe Embeddings:**
   - Visit [https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/)
   - Download the desired GloVe embedding file (e.g., `glove.6B.zip`)
   - Unzip the file and place the `.txt` embedding files inside the `embeddings/` folder in this project.

   - OR you could run the ./glove.sh script to do this automatically

## Usage

1. **Run the app:**
   ```bash
   streamlit run app.py
   ```


## Project Structure

```
emotion-detection/
│
├── embeddings/           # Place GloVe files here
├── data/                 # Dataset files
├── src/                  # Source code
├── train.py              # Training script
├── predict.py            # Prediction script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Notes

- Make sure the `embeddings/` folder contains the GloVe `.txt` files before running the code.
- For any issues, please open an issue on the repository.
