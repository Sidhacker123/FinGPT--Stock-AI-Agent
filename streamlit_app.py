
import streamlit as st
from agent.fin_agent import FinGPT
from auth import check_login
from utils.pdf_parser import extract_text_from_pdf
from utils.csv_parser import summarize_csv
import os
import json
from datetime import datetime

st.set_page_config(page_title="FinGPT", layout="centered")
if not check_login():
    st.stop()

st.title("💼 FinGPT: RAG-powered Financial Assistant")
agent = FinGPT()

# Document upload
st.markdown("### 📂 Upload Financial Document (PDF or CSV)")
uploaded = st.file_uploader("Choose a file", type=["pdf", "csv"])
if uploaded:
    os.makedirs("data/documents", exist_ok=True)
    fname = uploaded.name
    if fname.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded)
    elif fname.endswith(".csv"):
        text = summarize_csv(uploaded)
    else:
        st.error("Unsupported file.")
        st.stop()
    with open(f"data/documents/{fname}.txt", "w") as f:
        f.write(text)
    st.success(f"Uploaded and processed: {fname}")

# Build session log
if "history" not in st.session_state:
    st.session_state["history"] = []

query = st.text_input("Ask FinGPT a financial question:")
if query:
    with st.spinner("Thinking..."):
        response = agent.ask(query)
        answer = response['answer']
        st.session_state["history"].append({
            "query": query,
            "answer": answer,
            "docs": response["docs"]
        })
        st.markdown(f"### 🧠 Answer\n{answer}")
        st.markdown("### 📚 Sources")
        for doc in response['docs']:
            st.markdown(f"- **{doc['source']}** — Score: {doc['score']:.2f}")

# Session export
if st.button("📥 Export Session to Markdown"):
    os.makedirs("export", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    md_path = f"export/session_{timestamp}.md"
    with open(md_path, "w") as f:
        for h in st.session_state["history"]:
            f.write(f"## Question: {h['query']}\n")
            f.write(f"**Answer:** {h['answer']}\n\n")
            for doc in h['docs']:
                f.write(f"- Source: {doc['source']}, Score: {doc['score']:.2f}\n")
            f.write("\n---\n\n")
    st.success(f"Session exported: {md_path}")
