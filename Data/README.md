## Data Preparation
This folder contains all datasets, intermediate outputs, and preprocessing steps used in the QMSS–IBM Practicum Project.

Our project focuses on supporting the HHS Enterprise Performance Life Cycle (EPLC) process using generative AI and Retrieval-Augmented Generation (RAG), by building a structured knowledge base from publicly available documents and templates. 

## 1. Overview
Data Source: 
- EPLC Templates: https://web.archive.org/web/20240609100355/https:/www2.cdc.gov/cdcup/library/templates/default.htm#sthash.UcHHkg85.cHHkg856.dpbs
- EPLC Policy: https://www.hhs.gov/web/governance/digital-strategy/it-policy-archive/policy-for-information-technology-enterprise-performance.html

Raw Data Format: docx, xls

Final Output Format: JSON

Templates Size: 17 documents

## 2. Folder Contents
### 📥 Extractiond
| File | Description |
|------|-------------|
| `xxx.docx` | Original Templates. |
| `xxx.json` | Data after chunked and flattened. |

### 🧹 Cleaning
| File | Description |
|------|-------------|
| `xxx_embedding.json` | Texts converted into embeddings. |
| `xxx Phase DB.py` | Codes that turn embeddings into Vector DB. |

### 📦 Final Outputs
| File | Description |
|------|-------------|
| `chroma_db_xxx` | Final Vector DB that are ready to perform generative AI. |


## 3. Embedding Model Overview
Model name: BAAI/bge-large-en-v1.5

Model size: 0.3B params

Dimension: 1024

Advantage: Trained specifically for retrieval, not general-purpose tasks, optimized for English long-text retrieval (important for EPLC), and worked extremely well with vector databases (Chroma)

