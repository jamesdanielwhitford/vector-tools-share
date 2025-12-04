# Vector Tools Setup & Usage

## Overview

This repository provides a ChromaDB vector store for querying Sentry documentation and blog content. Use it to fact-check claims, research technical topics, and verify content accuracy when writing articles about Sentry.

## Directory Structure

```
vector-tools-share/
├── README.md              # This file
├── AGENTS.md              # Instructions for AI coding assistants
├── vector-tools/          # Vector database tools
│   ├── ingest.py          # Script to add content to vector store
│   ├── query.py           # Script to search vector store
│   ├── requirements.txt   # Python dependencies
│   ├── venv/              # Python virtual environment (you'll create this)
│   └── vectorstore/       # ChromaDB database (created after ingestion)
├── code/                  # For testing code examples
└── research/              # For fact-checking research
```

## Setup Instructions

### 1. Create Python Virtual Environment

```bash
cd vector-tools
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Ingest Content into Vector Store

The `ingest.py` script accepts GitHub URLs pointing to specific folders. When you provide a URL like `https://github.com/getsentry/sentry-docs/tree/master/docs`, it:

1. Clones the repository
2. Extracts only the `/docs` folder from the `master` branch
3. Loads all `.md`, `.mdx`, and `.txt` files
4. Splits them into 800-character chunks with 200-character overlap
5. Creates embeddings and stores them in ChromaDB
6. Tags all content with `group: "sentry"` metadata

**Option A: Automated Setup (Recommended)**

Run the provided setup script to ingest all required repositories:

```bash
chmod +x setup_vectorstore.sh
./setup_vectorstore.sh
```

This script ingests:
- `https://github.com/ritza-co/sentry`
- `https://github.com/getsentry/sentry-docs/tree/master/docs`

**Option B: Manual Ingestion**

To manually ingest repositories:

```bash
# First repository (creates new vector store)
./venv/bin/python ingest.py https://github.com/ritza-co/sentry/tree/main/blog

# Subsequent repositories (append with --append flag)
./venv/bin/python ingest.py https://github.com/ritza-co/sentry/tree/main/guides --append
./venv/bin/python ingest.py https://github.com/ritza-co/sentry/tree/main/refresh-articles --append
./venv/bin/python ingest.py https://github.com/getsentry/sentry-docs/tree/master/docs --append
```

Use `--append` to add content to an existing vector store instead of replacing it.

### 4. Query the Vector Store

```bash
./venv/bin/python query.py "your search query here"
```

**Example queries:**
```bash
./venv/bin/python query.py "OTLP tracing"
./venv/bin/python query.py "error monitoring best practices"
./venv/bin/python query.py "Node.js performance monitoring"
```

The script returns the top 5 most relevant chunks as JSON with:
- `text`: The content chunk
- `source`: Original file path
- `group`: Metadata tag (always "sentry")

## How It Works

### Vector Embeddings

The system uses `all-MiniLM-L6-v2` sentence transformers to create semantic embeddings. When you query, it finds the most semantically similar content chunks, not just keyword matches.

### GitHub Folder URLs

When you provide a GitHub URL like:
```
https://github.com/getsentry/sentry-docs/tree/master/docs
```

The script parses:
- `getsentry/sentry-docs` - Repository
- `master` - Branch
- `docs` - Folder path

It performs a shallow clone (`depth=1`) to minimize download size, then extracts only the specified folder.

## Using with AI Coding Assistants

The `CLAUDE.md` file contains instructions that enable AI assistants (Claude Code, etc.) to collaborate with you on technical writing projects using the vector tools.

**How it works:**
- The AI assistant reads `CLAUDE.md` to understand the collaborative writing workflow
- You work **with** the AI assistant, not asking it to write autonomously
- The AI helps you research, test code, create structure, and flesh out content based on your direction
- This ensures articles are accurate, well-tested, and properly sourced

**Collaborative Writing Workflow:**

The writer and AI assistant work together through these phases:

### 1. Research Phase
- Writer requests specific research queries
- AI queries vector store for relevant documentation, examples, and patterns
- AI documents findings in `research/` folder with sources
- Writer reviews research to inform article direction

### 2. Code Development Phase
- Writer specifies what code examples are needed
- AI writes code based on research findings
- AI tests code to verify it works correctly
- Writer reviews and approves working code
- Tested code stored in `code/` folder

### 3. Structure Phase
- Writer reviews writing rules, good example article, and developer-focused writing guidelines
- Writer and AI collaborate to create article skeleton/outline in `draft.md`
- Structure follows best practices for technical documentation

### 4. Content Creation Phase
- Writer directs AI section-by-section through the draft
- AI fleshes out each section using:
  - Verified code from `code/` folder
  - Research data from `research/` folder
  - Vector store queries for specific technical details
  - Writing rules and style guidelines
- Writer reviews and refines each section iteratively

### Example Workflow

**Not this:** "Write me a Node.js logging article"

**But this:**
1. Writer: "Query the vector store for existing Node.js logging content"
2. AI: Queries and documents findings in `research/`
3. Writer: "Create a basic Node.js logging example using Winston"
4. AI: Writes and tests code in `code/`
5. Writer: "Create an article outline based on the good example article structure"
6. AI: Creates skeleton in `draft.md`
7. Writer: "Flesh out the introduction section using our research"
8. AI: Writes introduction with proper sources
9. Writer: "Now the setup section, include the tested Winston code"
10. AI: Adds content with working code example
11. *Continue section by section...*

**Note:** Make sure your AI coding assistant loads the `CLAUDE.md` file at the start of each session so it understands the collaborative workflow.

## Customizing Query Results

Edit `vector-tools/query.py` to adjust:
- `k=5` (line 35): Number of results returned
- `filter={"group": "sentry"}` (line 36): Metadata filtering
- Add relevance scoring or additional filters as needed

## Troubleshooting

**Virtual environment not activating:**
```bash
# Make sure you're in the vector-tools directory
cd vector-tools
# Try with python3 explicitly
python3 -m venv venv
```

**Ingestion fails:**
- Ensure you have git installed (`git --version`)
- Check internet connection for GitHub access
- Verify the GitHub URL is correctly formatted

**Query returns no results:**
- Verify the vector store was created: `ls vectorstore/`
- Check if ingestion completed successfully
- Try broader search terms

## Dependencies

- Python 3.8+
- langchain-community
- chromadb
- sentence-transformers
- gitpython

See `requirements.txt` for complete list.
