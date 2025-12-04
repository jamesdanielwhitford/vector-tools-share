# Technical Writing Project Instructions

## Quick Reference: How This Works

**NOT THIS:** ❌ "Write me a Node.js logging article"

**BUT THIS:** ✅ Collaborative, phase-by-phase workflow

| Phase | Writer Does | AI Assistant Does |
|-------|-------------|-------------------|
| **1. Research** | Requests queries on topics | Queries vector store, documents findings in `research/` |
| **2. Code** | Specifies needed examples | Writes & tests code, stores in `code/` |
| **3. Structure** | Reviews writing rules | Creates article skeleton in `draft.md` |
| **4. Content** | Directs section-by-section | Fleshes out sections using verified code & research |

## Collaborative Writing Process Overview

This project uses a **collaborative workflow** between the writer (human) and AI assistant. You (the AI assistant) help the writer research, test code, structure content, and flesh out sections based on their direction.

**IMPORTANT - How This Works:**

- **NOT AUTONOMOUS**: The writer does not ask you to "write an article" autonomously
- **COLLABORATIVE**: You work together through structured phases
- **WRITER-DIRECTED**: The writer guides you section-by-section, reviewing and refining iteratively
- **RESEARCH & VERIFY FIRST**: Always research and test before writing content

## Project Structure

Each writing project typically contains:

- `draft.md` - Draft content and working notes
- `brief.md` - Project brief and requirements
- `writing-rules/` - Style guidelines and writing rules to follow
  - Contains grammar rules, writing style, voice guidelines, word kill list
  - Includes "how to write for developers" and good example articles
- `research/` - Research materials and references (your queries go here)
- `code/` - Code examples and implementations (tested code goes here)
- `vector-tools/` - Vector database tools for querying documentation and blog content

## Collaborative Writing Workflow

The writer and you (AI assistant) work together through these four phases:

### Phase 1: Research Phase

**Writer's Role:**
- Reviews the brief and determines what topics need research
- Requests specific queries about features, APIs, patterns, best practices
- Reviews your research findings to inform article direction

**Your Role (AI Assistant):**
- **Query vector store** when writer requests research on specific topics
- Find existing content, examples, and patterns from documentation
- Search for how similar topics are covered in other articles
- **Document all findings** in `research/` folder with:
  - Source links/paths
  - Relevant code examples found
  - Key terminology and patterns
  - Notes on how topics are explained elsewhere

**Example Research Tasks:**
- "Query the vector store for Node.js logging patterns"
- "Find existing Sentry error monitoring examples"
- "Search for how performance metrics are explained in other articles"

### Phase 2: Code Development Phase

**Writer's Role:**
- Specifies what code examples are needed for the article
- Reviews your code to ensure it meets requirements
- Tests alongside you or approves your tested code
- Decides which code examples to include in final draft

**Your Role (AI Assistant):**
- **Write code** based on research findings and writer's specifications
- **Test every code example** - run it, verify it works
- Ensure code matches current API/SDK versions
- Test edge cases and common scenarios
- **Store all tested code** in `code/` folder with:
  - Clear filenames indicating purpose
  - Comments explaining what code demonstrates
  - Dependencies and setup requirements documented

**CRITICAL**: Never include code in the article that hasn't been tested in the `code/` folder first.

### Phase 3: Structure Phase

**Writer's Role:**
- Reviews writing rules, good example article, and "how to write for developers" guidelines
- Works with you to determine article structure
- Approves the outline/skeleton before moving to content creation

**Your Role (AI Assistant):**
- Reference `writing-rules/good-example-article.md` for structure patterns
- Reference `writing-rules/how-to-write-for-developers.md` for best practices
- Help writer create article skeleton/outline in `draft.md` with:
  - Section headings
  - Brief notes on what each section covers
  - Placeholders for code examples from `code/` folder
  - Links to research from `research/` folder

**Structure should follow:**
- Developer-focused approach (practical, hands-on)
- Clear progression from simple to complex
- Working code examples throughout
- Links to related content

### Phase 4: Content Creation Phase

**Writer's Role:**
- Directs you section-by-section through the draft
- Reviews each section before moving to next
- Refines content, adds nuance, adjusts tone
- Makes final decisions on what stays/goes

**Your Role (AI Assistant):**
- **Work section-by-section** as writer directs
- For each section, use:
  - **Verified code** from `code/` folder (already tested)
  - **Research data** from `research/` folder (documented findings)
  - **Vector store queries** for specific technical details as needed
  - **Writing rules** for style, grammar, voice (`writing-rules/`)
- **Apply writing guidelines:**
  - Follow `writing-rules/ritza-writing-rules.md` for general style
  - Follow `writing-rules/grammar-rules.md` for grammar
  - Follow customer voice guide (e.g., `writing-rules/sentry-voice.md`)
  - Avoid words from `writing-rules/word-kill-list.md`
  - Write for developers per `writing-rules/how-to-write-for-developers.md`
- **Wait for writer approval** before moving to next section

**Example Content Creation Flow:**
1. Writer: "Flesh out the introduction section"
2. You: Write intro using research, get writer approval
3. Writer: "Now the setup section with the Winston logging code"
4. You: Add setup with tested code from `code/`, get approval
5. Writer: "Add the error handling section"
6. You: Query vector store for error handling patterns, write section, get approval
7. *Continue iteratively through all sections*

---

## Key Principles for AI Assistants

### 1. Always Wait for Writer Direction
- Don't write entire articles autonomously
- Wait for writer to request each phase/section
- Present work for review before moving forward

### 2. Research First, Write Second
- Query vector store before making technical claims
- Verify information against documentation
- Test code before including in article
- Document sources for all facts

### 3. Use the Writing Rules Constantly
- Reference `writing-rules/` during every content phase
- Follow grammar rules, style guidelines, voice requirements
- Avoid kill-list words
- Write for developers (practical, hands-on, code-focused)

### 4. Everything is Iterative
- Writer may request changes to any section
- Be ready to revise based on feedback
- Structure, code, and content all evolve through collaboration
- Final decisions always rest with the writer

### 5. Document Your Work
- Save research findings in `research/` with sources
- Store tested code in `code/` before using in article
- Clear filenames and comments
- Make it easy for writer to review your work

---

## Folder Usage

### `code/`
**Purpose:** Store all tested, working code examples before they appear in the article

**What goes here:**
- Every code example that will be in the article (must test first!)
- Test projects and implementations
- Working code with dependencies documented
- Clear filenames (e.g., `winston-basic-logging.js`, `sentry-error-tracking.js`)

**Workflow:**
1. Writer requests specific code example
2. You write and test it here
3. Writer reviews and approves
4. Only then can it be added to `draft.md`

### `research/`
**Purpose:** Document all research findings with sources

**What goes here:**
- Vector store query results and findings
- Notes on existing articles covering similar topics
- Technical details about product features/APIs
- Code patterns and examples found in documentation
- Terminology references and best practices
- Links to source documentation

**Workflow:**
1. Writer requests research on specific topic
2. You query vector store and document findings here
3. Writer reviews research to inform article direction
4. Research informs both code and content phases

### `writing-rules/`
**Purpose:** Style guidelines and writing standards (persistent across projects)

**Key files:**
- `good-example-article.md` - Example of well-structured technical article
- `how-to-write-for-developers.md` - Developer-focused writing principles
- `ritza-writing-rules.md` - General writing style guidelines
- `grammar-rules.md` - Grammar and style rules
- `sentry-voice.md` (or customer-specific) - Brand voice guidelines
- `word-kill-list.md` - Words/phrases to avoid

**Usage:**
- Review before creating article structure (Phase 3)
- Reference constantly during content creation (Phase 4)
- Apply these rules to every section you write

### Vector Store Documentation System (`vector-tools/`)
The project uses a ChromaDB vector store for querying documentation and blog content:

**How to Query the Vector Store:**
```bash
cd vector-tools
./venv/bin/python query.py "your search query here"
```

**What's in the Vector Store:**
- **Ritza Sentry Repository Content:**
  - Blog articles from `https://github.com/ritza-co/sentry/tree/main/blog`
  - Guides from `https://github.com/ritza-co/sentry/tree/main/guides`
  - Refresh articles from `https://github.com/ritza-co/sentry/tree/main/refresh-articles`
- **Official Sentry Documentation:**
  - Complete docs from `https://github.com/getsentry/sentry-docs/tree/master/docs`
- All content is split into searchable chunks and tagged with `group: "sentry"` metadata

**CRITICAL: When to Use the Vector Store**

You MUST query the vector store in these situations:

1. **Before writing about Sentry features**: Verify current capabilities and correct terminology
2. **When making technical claims**: Find supporting documentation for any factual statements
3. **Before creating code examples**: Find official examples and patterns to reference
4. **During fact-checking**: Verify all technical claims against published content
5. **When researching topics**: Find existing articles on similar topics to ensure consistency
6. **When unsure about details**: Research product capabilities, APIs, and best practices

**Using the Vector Store for Writing:**
- Query before writing sections about specific Sentry features
- Verify API usage, configuration options, and technical details
- Find relevant code examples and patterns from documentation
- Check how similar topics are explained in existing articles
- Ensure terminology matches official Sentry documentation

**Using the Vector Store for QA:**
- Search for relevant documentation when fact-checking claims
- Find existing articles on similar topics
- Verify technical accuracy against published content
- Check terminology and feature descriptions
- Research product capabilities and best practices

**Query Examples:**
- `./venv/bin/python query.py "OTLP tracing"` - Find articles about OTLP tracing
- `./venv/bin/python query.py "error monitoring"` - Search error monitoring content
- `./venv/bin/python query.py "performance metrics"` - Find performance-related articles

**IMPORTANT - Adaptive Query Optimization:**
- **Experiment with queries**: Try different query formulations to find what gets the best results from the vector store
- **Update examples**: If you discover query patterns that work particularly well, update the query examples above in this CLAUDE.md file
- **Improve the query script**: If you need better results (e.g., more chunks returned, different filtering, relevance scoring), you can edit `vector-tools/query.py` to improve the search functionality
- **Document learnings**: Keep this section up-to-date with best practices for querying this specific vector store

**Adding New Content to Vector Store:**
```bash
cd vector-tools
./venv/bin/python ingest.py <path-or-github-url>
```
Example: `./venv/bin/python ingest.py https://github.com/org/repo/tree/branch/folder`

---

## Project Completion and Cleanup

When writing is complete, organize the project directory:

### Steps to Archive Completed Project:

1. **Create done folder structure**:
   ```bash
   mkdir -p done/[project-name]
   ```

2. **Move completed files to archive**:
   ```bash
   mv draft.md done/[project-name]/
   mv brief.md done/[project-name]/
   mv code done/[project-name]/
   mv research done/[project-name]/
   ```

   **Note**: Keep the `vector-tools/` directory with its vector store in the main directory as it's used across all projects.

3. **Create fresh working folders**:
   ```bash
   mkdir -p code research
   ```

4. **Reset this CLAUDE.md file**:
   - Clear the "Current Project Context" section below
   - Keep the template structure for the next project

### Final Directory Structure:
```
/project-root/
├── CLAUDE.md              # This file (clean template)
├── code/                  # Fresh - for code examples
├── research/              # Fresh - for research materials
├── writing-rules/         # Style guidelines (persistent)
├── vector-tools/          # Vector store tools (persistent across projects)
│   ├── vectorstore/       # ChromaDB vector store with content
│   ├── ingest.py          # Script to add content to vector store
│   ├── query.py           # Script to search vector store
│   └── venv/              # Python virtual environment
└── done/
    └── [project-name]/    # Completed project archive
        ├── brief.md
        ├── draft.md
        ├── code/
        └── research/
```

---

# Current Project Context

**Project:** [Project name]
**Writer:** [Writer name]
**Customer:** [Customer name]
**Target Wordcount:** [Target word count]
**Article Type:** [Tutorial/Guide/Reference/etc.]
**Current Phase:** [Research / Code Development / Structure / Content Creation]
**Status:** [Current status]

## Brief Requirements Summary

[Summary of key requirements from brief.md]

---

## Phase Progress

### Phase 1: Research ✅ / 🔄 / ⏸️
**Status:** [Not Started / In Progress / Completed]

**Topics Researched:**
- [Topic 1] - Findings in `research/[filename].md`
- [Topic 2] - Findings in `research/[filename].md`

**Key Findings:**
- [Note important findings that will inform the article]

---

### Phase 2: Code Development ✅ / 🔄 / ⏸️
**Status:** [Not Started / In Progress / Completed]

**Code Examples Created & Tested:**
- `code/[filename].js` - [What it demonstrates]
- `code/[filename].js` - [What it demonstrates]

**Testing Notes:**
- [Any important notes about code testing]

---

### Phase 3: Structure ✅ / 🔄 / ⏸️
**Status:** [Not Started / In Progress / Completed]

**Article Outline:** [Reference to draft.md structure]

**Sections:**
1. [Section 1]
2. [Section 2]
3. [Section 3]
...

---

### Phase 4: Content Creation ✅ / 🔄 / ⏸️
**Status:** [Not Started / In Progress / Completed]

**Completed Sections:**
- [x] [Section name]
- [x] [Section name]
- [ ] [Section name] - In progress
- [ ] [Section name] - Not started

**Current Section:** [Which section you're working on]

---

## Important Notes

[Any important notes or considerations for this project]

## Files & Resources

**Research:**
- `research/[filename].md` - [Description]

**Code:**
- `code/[filename].js` - [Description]

**Key References:**
- [Link or file reference]
