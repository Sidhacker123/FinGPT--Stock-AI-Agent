
import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def build_faiss_index(doc_folder="data/documents", index_file="data/faiss.index", meta_file="data/faiss_meta.json"):
    texts = []
    embeddings = []
    for fname in os.listdir(doc_folder):
        with open(os.path.join(doc_folder, fname), 'r') as f:
            text = f.read()
        texts.append({"file": fname, "text": text})
        emb = model.encode(text)
        embeddings.append(emb)
    vectors = np.vstack(embeddings).astype("float32")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    faiss.write_index(index, index_file)
    with open(meta_file, "w") as f:
        json.dump(texts, f, indent=4)

def search_faiss(query, index_file="data/faiss.index", meta_file="data/faiss_meta.json", top_k=3):
    index = faiss.read_index(index_file)
    with open(meta_file) as f:
        texts = json.load(f)
    q_vec = model.encode(query).astype("float32").reshape(1, -1)
    D, I = index.search(q_vec, top_k)
    return [{"source": texts[i]["file"], "content": texts[i]["text"], "score": float(D[0][j])} for j, i in enumerate(I[0])]
