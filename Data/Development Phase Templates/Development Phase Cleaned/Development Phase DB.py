import json
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer


json_files = [
    "Training Plan.json",
    "Test Case.json",
    "Operation.json"
]

rows = []


for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for section in data["sections"]:
        rows.append({
            "document": data["document_title"],
            "section_number": section["number"],
            "section_title": section["title"],
            "text": section.get("content") or ""
        })
        for sub in section.get("subsections", []):
            rows.append({
                "document": data["document_title"],
                "section_number": sub["number"],
                "section_title": sub["title"],
                "text": sub.get("content") or ""
            })

df = pd.DataFrame(rows)

model = SentenceTransformer("BAAI/bge-large-en-v1.5")
df["embedding"] = df["text"].apply(lambda x: model.encode(x).tolist())
for doc_title, doc_df in df.groupby("document"):
    safe_name = doc_title.replace(" ", "_").replace("/", "_")
    out_path = f"{safe_name}_embedding.json"
    doc_df.to_json(out_path, orient="records", indent=2, force_ascii=False)
    print(f"Saved embedding file: {out_path}")


chroma_path = "/Users/adonischeng/Desktop/QMSS_IBM_Practicum_2025Fall/Data/Vector DataBase/chroma_db_development_phase"
chroma_client = chromadb.PersistentClient(path=chroma_path)
collection = chroma_client.get_or_create_collection("development_phase_templates")

ids = [f"{row['document']}_{row['section_number']}_{i}" for i, row in df.iterrows()]

collection.add(
    ids=ids,
    documents=df["text"].tolist(),
    embeddings=df["embedding"].tolist(),
    metadatas=[
        {"document": row["document"], "section_number": row["section_number"], "section_title": row["section_title"]}
        for _, row in df.iterrows()
    ]
)