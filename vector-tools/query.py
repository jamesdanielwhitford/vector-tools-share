#!/usr/bin/env ./venv/bin/python
import sys
import json
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
VECTORSTORE_PATH = "vectorstore"
COLLECTION_NAME = "docs"

def main(query):
    """
    Queries the ChromaDB vector store for documents related to the query.
    """
    if not query:
        print("Error: No query provided.")
        print("Usage: python query.py \"Your query here\"")
        return

    print(f"Querying for: '{query}'")

    # Load embeddings model
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Load Chroma vector store
    vectorstore = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )

    # Perform similarity search with metadata filtering
    results = vectorstore.similarity_search(
        query,
        k=5,  # Return top 5 results
        filter={"group": "sentry"}
    )

    # Format and print results
    output = []
    for doc in results:
        output.append({
            "text": doc.page_content,
            "source": doc.metadata.get("source"),
            "group": doc.metadata.get("group")
        })

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python query.py \"<your search query>\"")
    else:
        main(sys.argv[1])
