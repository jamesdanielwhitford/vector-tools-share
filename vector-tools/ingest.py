#!/usr/bin/env ./venv/bin/python
import os
import shutil
import argparse
import tempfile
from git import Repo
from urllib.parse import urlparse
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
VECTORSTORE_PATH = "vectorstore"
COLLECTION_NAME = "docs"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200
ALLOWED_EXTENSIONS = [".md", ".mdx", ".txt"]

# --- Helper Functions ---
def is_github_url(path):
    """Checks if the given path is a GitHub URL."""
    return urlparse(path).hostname == "github.com"

def handle_github_repo(url):
    """
    Clones a GitHub repository from a URL.
    Handles both:
    - Repository root URLs: https://github.com/<org>/<repo>
    - Specific folder URLs: https://github.com/<org>/<repo>/tree/<branch>/<folder>

    Returns the local path to the repository or folder, and the temp directory to clean up.
    """
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")

    # Validate we have at least org/repo
    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub URL. Expected format: https://github.com/<org>/<repo> or https://github.com/<org>/<repo>/tree/<branch>/<folder>")

    org = path_parts[0]
    repo_name = path_parts[1]
    repo_url = f"https://github.com/{org}/{repo_name}.git"

    # Check if this is a repository root URL or a tree URL
    if len(path_parts) == 2:
        # Repository root URL: https://github.com/<org>/<repo>
        temp_dir = tempfile.mkdtemp()
        print(f"Cloning entire repository {repo_url} into temporary directory {temp_dir}...")
        Repo.clone_from(repo_url, temp_dir, depth=1)
        return temp_dir, temp_dir

    elif len(path_parts) >= 3 and path_parts[2] == "tree":
        # Folder-specific URL: https://github.com/<org>/<repo>/tree/<branch>/<folder>
        if len(path_parts) < 4:
            raise ValueError("Invalid GitHub tree URL. Expected format: https://github.com/<org>/<repo>/tree/<branch> or https://github.com/<org>/<repo>/tree/<branch>/<folder>")

        branch = path_parts[3]
        folder_path = "/".join(path_parts[4:]) if len(path_parts) > 4 else ""

        temp_dir = tempfile.mkdtemp()
        print(f"Cloning {repo_url} (branch: {branch}) into temporary directory {temp_dir}...")
        Repo.clone_from(repo_url, temp_dir, branch=branch, depth=1)

        # If a folder path is specified, use it; otherwise use the repo root
        if folder_path:
            local_docs_path = os.path.join(temp_dir, folder_path)
            if not os.path.isdir(local_docs_path):
                shutil.rmtree(temp_dir)
                raise FileNotFoundError(f"The folder '{folder_path}' was not found in the repository.")
            return local_docs_path, temp_dir
        else:
            return temp_dir, temp_dir

    else:
        raise ValueError("Invalid GitHub URL format. Expected: https://github.com/<org>/<repo> or https://github.com/<org>/<repo>/tree/<branch>/<folder>")

def load_documents(docs_path):
    """Loads documents from the specified directory."""
    print(f"Loading documents from: {docs_path}")
    
    # Create a glob pattern for all allowed file extensions
    glob_pattern = "**/*[{}]".format("".join(ALLOWED_EXTENSIONS))
    
    loader = DirectoryLoader(
        docs_path,
        glob=glob_pattern,
        loader_cls=TextLoader,
        recursive=True,
        show_progress=True,
        use_multithreading=True
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")
    return documents

def split_documents(documents):
    """Splits documents into manageable chunks."""
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")
    return chunks

def create_embeddings_and_store(chunks, append=False):
    """Creates embeddings and stores them in ChromaDB."""
    print("Creating embeddings and storing in ChromaDB...")

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    for chunk in chunks:
        chunk.metadata["group"] = "sentry"

    if os.path.exists(VECTORSTORE_PATH) and not append:
        print(f"Removing existing vector store at {VECTORSTORE_PATH}...")
        shutil.rmtree(VECTORSTORE_PATH)

    # ChromaDB has a max batch size limit (~5461), so we need to batch large collections
    BATCH_SIZE = 5000
    total_chunks = len(chunks)

    if os.path.exists(VECTORSTORE_PATH) and append:
        print(f"Appending to existing vector store at {VECTORSTORE_PATH}...")
        vectorstore = Chroma(
            persist_directory=VECTORSTORE_PATH,
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )
        # Process in batches
        for i in range(0, total_chunks, BATCH_SIZE):
            batch = chunks[i:i + BATCH_SIZE]
            batch_num = (i // BATCH_SIZE) + 1
            total_batches = (total_chunks + BATCH_SIZE - 1) // BATCH_SIZE
            print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} documents)...")
            vectorstore.add_documents(batch)
    else:
        print(f"Creating new vector store at {VECTORSTORE_PATH}...")
        # For initial creation, use first batch with from_documents, then append rest
        first_batch = chunks[:BATCH_SIZE]
        vectorstore = Chroma.from_documents(
            documents=first_batch,
            embedding=embeddings,
            collection_name=COLLECTION_NAME,
            persist_directory=VECTORSTORE_PATH
        )
        print(f"Created vector store with first batch ({len(first_batch)} documents)...")

        # Add remaining batches if there are any
        if total_chunks > BATCH_SIZE:
            remaining_chunks = chunks[BATCH_SIZE:]
            total_batches = (len(remaining_chunks) + BATCH_SIZE - 1) // BATCH_SIZE
            for i in range(0, len(remaining_chunks), BATCH_SIZE):
                batch = remaining_chunks[i:i + BATCH_SIZE]
                batch_num = (i // BATCH_SIZE) + 2  # +2 because first batch was already added
                print(f"Adding batch {batch_num}/{total_batches + 1} ({len(batch)} documents)...")
                vectorstore.add_documents(batch)

    print("Ingestion complete!")
    return vectorstore

def main():
    """Main function to run the ingestion process."""
    parser = argparse.ArgumentParser(description="Ingest documents from a local folder or a GitHub repository.")
    parser.add_argument("path", type=str, help="Path to a local folder or a GitHub URL. Supports: (1) Local path, (2) Repository root (e.g., https://github.com/ritza-co/sentry), or (3) Specific folder (e.g., https://github.com/getsentry/sentry-docs/tree/master/docs).")
    parser.add_argument("--append", action="store_true", help="Append to existing vector store instead of replacing it.")
    args = parser.parse_args()

    temp_dir_to_clean = None
    docs_path = args.path

    try:
        if is_github_url(docs_path):
            docs_path, temp_dir_to_clean = handle_github_repo(docs_path)
        elif not os.path.isdir(docs_path):
            raise ValueError(f"The provided local path is not a valid directory: {docs_path}")

        documents = load_documents(docs_path)
        chunks = split_documents(documents)
        create_embeddings_and_store(chunks, append=args.append)

        print("\nIngestion process finished successfully.")
        print(f"Vector store at: {VECTORSTORE_PATH}")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
    finally:
        if temp_dir_to_clean:
            print(f"Cleaning up temporary directory: {temp_dir_to_clean}")
            shutil.rmtree(temp_dir_to_clean)

if __name__ == "__main__":
    main()
