
from rag.nemo_retriever import live_retrieve
from llm.llama3_client import call_nim_llm

def rag_answer(query):
    docs = live_retrieve(query)
    context = "\n".join([d["content"] for d in docs if "content" in d])
    prompt = f"Answer the question using the context below.\nContext:\n{context}\n\nQuestion: {query}"
    answer = call_nim_llm(prompt)
    return {"answer": answer, "docs": docs}
