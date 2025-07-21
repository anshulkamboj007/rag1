# vector_store.py

import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from data_ingestion import load_pdf_text
from data_cleaning import clean_text
from data_chunking import split_by_chapters
from variables import VECTORSTORE_PATH, SUMMARY_STORE_PATH,PDF_FILE
from llm_chain import summarize_func,get_embedding_model

class VectorStoreManager:
    def __init__(self):
        self.embed_model = get_embedding_model()

    def _load_vectorstore(self, path: str) -> FAISS:
        return FAISS.load_local(path, embeddings=self.embed_model, allow_dangerous_deserialization=True)

    def _save_vectorstore(self, docs: list[Document], path: str) -> FAISS:
        vs = FAISS.from_documents(docs, self.embed_model)
        vs.save_local(path)
        return vs

    def get_chapter_vectorstore(self) -> FAISS:
        if os.path.exists(VECTORSTORE_PATH):
            print("✅ Loading existing chapter vectorstore...")
            return self._load_vectorstore(VECTORSTORE_PATH)
        print("⚙️ Building chapter vectorstore...")
        raw = load_pdf_text(PDF_FILE)
        cleaned = clean_text(raw)
        chapters = split_by_chapters(cleaned)
        return self._save_vectorstore(chapters, VECTORSTORE_PATH)

    def get_summary_vectorstore(self, summarize_func) -> FAISS:
        # Ensure folder exists before saving
        os.makedirs(os.path.dirname(SUMMARY_STORE_PATH), exist_ok=True)

        if os.path.exists(SUMMARY_STORE_PATH):
            print("✅ Loading existing summary vectorstore...")
            return self._load_vectorstore(SUMMARY_STORE_PATH)

        print("⚙️ Generating summaries for vectorstore...")

        raw = load_pdf_text(PDF_FILE)
        cleaned = clean_text(raw)
        chapters = split_by_chapters(cleaned)

        summarized_docs = []
        print(f'total chapters found to be summarised .... {len(chapters)}')
        for i, doc in enumerate(chapters):
            summary = summarize_func(doc.page_content)
            
            if not summary.strip():
                print(f"⚠️ Chapter {i+1} returned an empty summary. Skipping.")
                continue

            print(f"📝 Summarizing chapter {i+1}...")
            summarized_docs.append(Document(
                page_content=summary,
                metadata=doc.metadata
            ))
            print(f"✅ Completed chapter {i+1}")

        print(f"📁 Saving summary vectorstore to {SUMMARY_STORE_PATH} ...")
        vs = self._save_vectorstore(summarized_docs, SUMMARY_STORE_PATH)
        print("✅ Summary vectorstore saved successfully.")

        return vs
