import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    index = faiss.read_index(os.path.join(BASE_DIR, "../vector.index"))
    chunks = np.load(os.path.join(BASE_DIR, "../chunks.npy"), allow_pickle=True)
    print("✅ Index and chunks loaded successfully")
except Exception as e:
    print("❌ Error loading index:", e)
    index = None
    chunks = None

def retrieve(query, k=2):
    if index is None or chunks is None:
        return ["Error: Index not loaded"]

    q_emb = model.encode([query])
    D, I = index.search(q_emb, k)
    results = [chunks[i] for i in I[0]]
    return results