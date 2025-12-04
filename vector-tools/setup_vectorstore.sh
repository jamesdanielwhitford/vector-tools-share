#!/bin/bash

# Setup script to populate the vector store with Sentry documentation and blog content
# This script ingests content from multiple GitHub repositories into a single ChromaDB vector store

set -e  # Exit on error

echo "========================================"
echo "Vector Store Setup"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run: python3 -m venv venv"
    echo "Then run: source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

PYTHON="./venv/bin/python"

# Array of repositories to ingest
REPOS=(
    "https://github.com/ritza-co/sentry"
    "https://github.com/getsentry/sentry-docs/tree/master/docs"
)

echo "This will ingest content from ${#REPOS[@]} repositories:"
for repo in "${REPOS[@]}"; do
    echo "  - $repo"
done
echo ""

# Ingest first repository (creates new vector store)
echo "========================================"
echo "Step 1/2: Ingesting Ritza blog content"
echo "========================================"
$PYTHON ingest.py "${REPOS[0]}"
echo ""

# Ingest remaining repositories (append to existing vector store)
echo "========================================"
echo "Step 2/2: Ingesting Ritza guides content"
echo "========================================"
$PYTHON ingest.py "${REPOS[1]}" --append
echo ""


echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Vector store is ready at: ./vectorstore"
echo ""
echo "To query the vector store, run:"
echo "  $PYTHON query.py \"your search query\""
echo ""
echo "Example queries:"
echo "  $PYTHON query.py \"Node.js logging\""
echo "  $PYTHON query.py \"error monitoring\""
echo "  $PYTHON query.py \"OTLP tracing\""
