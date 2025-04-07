
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

with open("data/embeddings.json") as f:
    db = json.load(f)

def retrieve(query, top_k=3):
    query_vec = model.encode(query)
    scores = [(doc, cosine_similarity([query_vec], [doc["embedding"]])[0][0]) for doc in db]
    ranked = sorted(scores, key=lambda x: -x[1])[:top_k]
    return [{"source": r[0]["file"], "content": r[0]["text"], "score": r[1]} for r in ranked]
