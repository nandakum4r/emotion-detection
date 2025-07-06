#!/bin/bash

set -e

EMBEDDINGS_DIR="$(dirname "$0")/../emotion-detection/embeddings"
ZIP_URL="http://nlp.stanford.edu/data/glove.6B.zip"
ZIP_FILE="$EMBEDDINGS_DIR/glove.6B.zip"
TXT_FILE="$EMBEDDINGS_DIR/glove.6B.300d.txt"

mkdir -p "$EMBEDDINGS_DIR"

# Download GloVe zip if not present
if [ ! -f "$ZIP_FILE" ]; then
    echo "Downloading GloVe embeddings..."
    curl -L "$ZIP_URL" -o "$ZIP_FILE"
else
    echo "GloVe zip already exists."
fi

# Extract 300d txt if not present
if [ ! -f "$TXT_FILE" ]; then
    echo "Extracting glove.6B.300d.txt..."
    unzip -j "$ZIP_FILE" "glove.6B.300d.txt" -d "$EMBEDDINGS_DIR"
    rm -f "$ZIP_FILE"
else
    echo "glove.6B.300d.txt already exists."
fi

