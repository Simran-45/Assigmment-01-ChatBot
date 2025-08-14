import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="EduAssist AI", layout="wide")
st.image("logo.jpg", use_container_width=True)

st.title("📚 EduAssist AI - Multi-PDF Smart Chatbot")

# Sidebar - Upload PDFs
uploaded_files = st.sidebar.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    docs = []
    metadata_mapping = []
    for uploaded_file in uploaded_files:
        # Save file locally
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        loader = PyPDFLoader(uploaded_file.name)
        file_docs = loader.load()
        for d in file_docs:
            d.metadata["source"] = uploaded_file.name  # Tag PDF name in metadata
        docs.extend(file_docs)

    # Create vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Select PDF in sidebar
    pdf_names = list(set([f.name for f in uploaded_files]))
    selected_pdf = st.sidebar.selectbox("Select a PDF to query:", pdf_names)

    query = st.text_input("💬 Ask a question or request a summary from the selected PDF:")

    if query:
        # Retrieve from only the chosen PDF
        retriever = vectorstore.as_retriever(search_kwargs={"filter": {"source": selected_pdf}})
        retrieved_docs = retriever.get_relevant_documents(query)

        # Apply reranking
        reranker = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-large")
        pairs = [(query, doc.page_content) for doc in retrieved_docs]
        scores = reranker.score(pairs)
        reranked_docs = [doc for _, doc in sorted(zip(scores, retrieved_docs), key=lambda x: x[0], reverse=True)]
        top_docs = reranked_docs[:4]
        context = "\n\n".join([d.page_content for d in top_docs])

        # Call LLM
        llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)
        prompt = f"Answer using only this PDF: {selected_pdf}\n\nContext:\n{context}\n\nQuestion: {query}"
        response = llm.invoke(prompt)

        st.markdown("### 📖 Answer")
        st.write(response.content)
else:
    st.info("Please upload one or more PDF files to get started.")
