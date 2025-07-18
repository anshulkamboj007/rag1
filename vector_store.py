import os
from langchain_community.vectorstores import FAISS
from data_ingestion import load_pdf_text
from data_cleaning import clean_text
from data_chunking import split_by_chapters
from variables import PDF_FILE,DATA_FOLDER,VECTORSTORE_PATH
from langchain_ollama import OllamaEmbeddings

def load_or_create_vectorstore(documents):
    embed_model=OllamaEmbeddings(model="mxbai-embed-large")

    if os.path.exists(VECTORSTORE_PATH):
        print("✅ Found existing vectorstore. Loading...")
        vectorstore=FAISS.load_local(VECTORSTORE_PATH,embeddings=embed_model,
                                     allow_dangerous_deserialization=True)
    else:
        print("⚙️ No vectorstore found. Rebuilding from PDF...")
        raw_text = load_pdf_text(PDF_FILE)
        cleaned_text = clean_text(raw_text)
        chapter_docs = split_by_chapters(cleaned_text)

        vectorstore=FAISS.from_documents(chapter_docs,embed_model)
        vectorstore.save_local(VECTORSTORE_PATH)
        print(f"📦 Saved new vectorstore to: {VECTORSTORE_PATH}")

    return vectorstore
