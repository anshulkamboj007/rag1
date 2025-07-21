from vector_store import VectorStoreManager
from llm_chain import summarize_func  # your custom LLM summary chain

vs_manager = VectorStoreManager()
chapter_vs = vs_manager.get_chapter_vectorstore()
summary_vs = vs_manager.get_summary_vectorstore(summarize_func)

retriever = chapter_vs.as_retriever()
summary_retriever = summary_vs.as_retriever()
