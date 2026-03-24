import faiss
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

index = faiss.read_index(os.path.join(BASE_DIR, "../vector.index"))
chunks = np.load(os.path.join(BASE_DIR, "../chunks.npy"), allow_pickle=True)
embeddings = np.load(os.path.join(BASE_DIR, "../embeddings.npy"))

def retrieve(query, k=2):
    # ❗ dummy simple approach (since no encoder)
    query_vector = embeddings[0:1]  # placeholder (cheap)

    D, I = index.search(query_vector, k)
    results = [chunks[i] for i in I[0]]
    return results