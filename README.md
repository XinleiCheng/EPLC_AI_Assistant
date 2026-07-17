# EPLC AI Assistant

EPLC AI Assistant is a prototype created for the Columbia University QMSS
Practicum in partnership with IBM. It explores how retrieval-augmented
generation (RAG) can help project managers navigate Enterprise Performance Life
Cycle guidance and draft EPLC deliverables.

The prototype focuses on four phases:

- Requirements Analysis
- Design
- Development
- Implementation

## Current status

This repository contains three parts that are not yet fully integrated:

- A Streamlit user-interface prototype in `ibm.py`
- Command-line RAG experiments for policy Q&A in `Coding/Q&A`
- Command-line document-drafting experiments in `Coding/Generation`

The Streamlit interface currently demonstrates the intended workflow but does
not yet call the Q&A or document-generation modules. Refactoring and integration
work is in progress.

## Intended workflow

1. Parse and chunk official EPLC guidance and templates.
2. Embed the chunks and store them in ChromaDB.
3. Retrieve relevant chunks for a project manager's question or selected
   document section.
4. Ask an OpenAI model to answer or draft using the retrieved context.
5. Show the supporting sources and flag information that still needs human
   confirmation.

AI-generated content is a drafting aid. It is not an official compliance
determination and should be reviewed by the responsible project team.

## Local setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add an OpenAI API key to `.env`, then start the current UI prototype:

```bash
streamlit run ibm.py
```

The existing RAG scripts also require local Chroma indexes. Their paths and
embedding configuration are being consolidated as part of the current
refactor.

## Repository guide

- `Coding/`: Q&A and document-generation experiments
- `Data/`: source documents, processed JSON, embeddings, and Chroma artifacts
- `frontend/`: duplicate of the current Streamlit prototype; scheduled for
  consolidation
- `Weekly Report/`: historical practicum presentation material

## Data sources

The data preparation notes and source links are documented in
[`Data/README.md`](Data/README.md).

<img width="1512" height="854" alt="EPLC Assistant prototype homepage" src="https://github.com/user-attachments/assets/1957b9f3-a4f2-491d-a07b-14f4a531b05d" />
