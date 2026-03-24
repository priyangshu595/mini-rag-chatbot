import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index("vector.index")
chunks = np.load("chunks.npy", allow_pickle=True)

def retrieve(query, k=3):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k)
    results = [chunks[i] for i in I[0]]
    return results
