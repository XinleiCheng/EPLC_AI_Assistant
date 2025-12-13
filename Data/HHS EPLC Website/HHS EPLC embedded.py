import json
import chromadb
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity



with open("HHS EPLC Website.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []


for section in data["sections"]:
    # Main section
    rows.append({
        "document": data["document_title"],
        "section_number": section["number"],
        "title": section["title"],
        "text": section["content"]
    })

    for sub in section.get("subsections", []):
        rows.append({
            "document": data["document_title"],
            "section_number": sub["number"],
            "title": sub["title"],
            "text": sub["content"]
        })

df = pd.DataFrame(rows)
print(f"{len(df)} text chunks for embedding.")

# Transform unstructured text into machine readable embeddings
model = SentenceTransformer("BAAI/bge-large-en-v1.5")  
df["embedding"] = df["text"].apply(lambda x: model.encode(x).tolist())
df.to_json("HHS_EPLC_embeddings.json", orient="records", indent=2, force_ascii=False)

# Create a ChromaDB collection and add all your text + embeddings + metadata into it
chroma_client = chromadb.PersistentClient(path="./chroma_eplc_policy")
collection = chroma_client.get_or_create_collection("hhs_eplc_policy")

ids = [f"section_{i}" for i in range(len(df))]

collection.add(
    ids=ids,
    documents=df["text"].tolist(),
    embeddings=df["embedding"].tolist(),
    metadatas=[
        {"document": row["document"], "section_number": row["section_number"], "s": row["title"]}
        for _, row in df.iterrows()
    ]
)

query = "What is the purpose of the EPLC policy?"
query_vec = model.encode(query).tolist()

results = collection.query(query_embeddings=[query_vec], n_results=3)

for i, doc in enumerate(results["documents"][0]):
    meta = results["metadatas"][0][i] or {}
    print(f" Result {i+1}")
    print(f"Title: {meta.get('title', 'N/A')}")
    print(f"Section: {meta.get('section_number', 'N/A')}")
    print(f"Text: {doc[:250]}...")


queries = [
    "What is the purpose of the EPLC policy?",
    "Who is responsible for managing the policy?",
    "What are the guiding principles of EPLC?",
    "When was this policy last updated?"
]

for q in queries:
    q_vec = model.encode(q)
    df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity([x], [q_vec])[0][0])
    top = df.sort_values(by="similarity", ascending=False).head(1)
    print(f"\n Query: {q}")
    print(f"Top Match: {top.iloc[0]['title']} (Section {top.iloc[0]['section_number']})")
    print(f"Similarity Rate: {top.iloc[0]['similarity']:.3f}")