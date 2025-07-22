import os
from preprocessing.data_ingestion import load_pdf_text
from preprocessing.data_cleaning import clean_text
from preprocessing.data_chunking import split_by_chapters
from variables import VECTORSTORE_PATH, SUMMARY_STORE_PATH, PDF_FILE
from llm_chain import get_embedding_model

from vectorstore.vector_loader import load_vectorstore
from vectorstore.vector_builder import build_vectorstore_from_docs
from vectorstore.vector_chunks import chunk_documents
from vectorstore.vector_summary import summarize_chapters

class VectorStoreManager:
    def __init__(self):
        self.embed_model = get_embedding_model()

    def get_chapter_vectorstore(self):
        if os.path.exists(VECTORSTORE_PATH):
            return load_vectorstore(VECTORSTORE_PATH, self.embed_model)

        raw = load_pdf_text(PDF_FILE)
        cleaned = clean_text(raw)
        chapters = split_by_chapters(cleaned)
        chunks = chunk_documents(chapters)
        return build_vectorstore_from_docs(chunks, self.embed_model, VECTORSTORE_PATH)

    def get_summary_vectorstore(self, summarize_func):
        os.makedirs(os.path.dirname(SUMMARY_STORE_PATH), exist_ok=True)

        if os.path.exists(SUMMARY_STORE_PATH):
            return load_vectorstore(SUMMARY_STORE_PATH, self.embed_model)

        raw = load_pdf_text(PDF_FILE)
        cleaned = clean_text(raw)
        chapters = split_by_chapters(cleaned)
        summaries = summarize_chapters(chapters, summarize_func)
        return build_vectorstore_from_docs(summaries, self.embed_model, SUMMARY_STORE_PATH)
