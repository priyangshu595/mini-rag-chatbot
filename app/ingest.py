import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_documents(folder="data"):
    docs = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
            docs.append(f.read())
    return docs

def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

documents = load_documents()

all_chunks = []
for doc in documents:
    all_chunks.extend(chunk_text(doc))

embeddings = model.encode(all_chunks)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

faiss.write_index(index, "vector.index")
np.save("chunks.npy", all_chunks)

print("Ingestion complete!")
