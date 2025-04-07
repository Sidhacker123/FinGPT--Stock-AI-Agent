
from sentence_transformers import SentenceTransformer
import os
import json

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def embed_docs(doc_folder='data/documents'):
    vectors = []
    for fname in os.listdir(doc_folder):
        with open(os.path.join(doc_folder, fname), 'r') as f:
            text = f.read()
        emb = model.encode(text)
        vectors.append({'file': fname, 'embedding': emb.tolist(), 'text': text})
    with open("data/embeddings.json", "w") as f:
        json.dump(vectors, f, indent=4)
