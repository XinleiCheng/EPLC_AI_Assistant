# IBM EPLC Chatbot - Core Features

This project features two primary modules: **Intelligent Q&A** and **Automated Document Generation**. Both leverage OpenAI's LLMs and ChromaDB vector storage to assist with the Enterprise Product Lifecycle (EPLC) workflow.

## 1. Q&A Module (Intelligent Querying)

The Q&A module enables users to query EPLC frameworks and HHS policies naturally. It utilizes **Retrieval-Augmented Generation (RAG)** to ensure answers are grounded in official documentation rather than generated from hallucination.

### Core Logic
The algorithms for this module are encapsulated in **`qna_finalv2.py`**. The workflow includes:

1.  **Hybrid Search Strategy:**
    * **Semantic Search:** Uses `SentenceTransformer` and ChromaDB to find conceptually related document chunks.
    * **Exact Keyword Match:** Scans for specific terminology or acronyms to improve precision.
    * **Threshold Filtering:** Automatically discards retrieved chunks that fall below a relevance score (`SEM_THRESHOLD`) to prevent noise.

2.  **Context Assembly & Answering:**
    * The system aggregates validated chunks from `EPLCFramework_db` and `HHS_db`.
    * **Strict Mode:** Prioritizes answering based solely on the provided context.
    * **Fallback Logic:** If `qna_finalv2.py` determines the context is insufficient ("Not specified in the provided context"), it can optionally pivot to general knowledge depending on configuration.

### Key File
* **`qna_finalv2.py`**:
    * Implements the full RAG pipeline (retrieval, re-ranking, prompt engineering).
    * Manages database connections and query logic.
    * Controls the fallback mechanism for "no context" scenarios.

---

## 2. Generation Module (Document Drafting)

The Generation module is a productivity tool designed to create "paste-ready" drafts for various EPLC project phases (Requirement, Design, Implementation, Development).

### Core Logic
The logic for generation, detection, and refinement is handled by **`Generation_final_v2.py`**:

1.  **Structured Drafting:**
    * Upon selecting a **Phase**, **Template**, and **Section**, the script loads the phase-specific vector database.
    * It processes user input (Key Details) to generate a professional draft (120–180 words) adhering to EPLC standards.

2.  **Missing Information Detection:**
    * **Parallel Analysis:** While generating the draft, `Generation_final_v2.py` runs a background check to identify critical missing elements (e.g., stakeholders, timelines, specific technologies).
    * **User Prompts:** It outputs a list of "Missing Required Information" to guide the user in providing more detail.

3.  **Iterative Refinement:**
    * **Regenerate:** Allows complete rewriting of the current draft.
    * **Follow-up Instructions:** Accepts natural language commands (e.g., *"Add details about cloud security"*) to refine the text without losing the original context.

### Key File
* **`Generation_final_v2.py`**:
    * Contains the System Prompts tailored for specific EPLC phases.
    * Implements the "Generate → Detect → Refine" loop.
    * Handles the logic for identifying missing project details.

---

## Quick Usage Guide

### Using Q&A
1.  Select **"Ask Question"** in the sidebar.
2.  Enter a question regarding EPLC processes or policies.
3.  **`qna_finalv2.py`** retrieves the relevant context and generates a precise answer.

### Using Generation
1.  Select **"Create Document"** in the sidebar.
2.  **Step 1:** Choose the Project Phase, Document Template, and Section.
3.  **Step 2:** Enter the Key Details for your project.
4.  **Step 3:** Click Generate. **`Generation_final_v2.py`** will output a draft and highlight any missing information. You can then refine or regenerate the draft using follow-up instructions.