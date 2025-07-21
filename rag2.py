# rag2.py

from vector_store import VectorStoreManager
from llm_chain import summarize_func, get_llm
from retriver import build_retrieval_qa

# Step 1: Get vectorstores
vs_manager = VectorStoreManager()
chapter_vs = vs_manager.get_chapter_vectorstore()
summary_vs = vs_manager.get_summary_vectorstore(summarize_func)

# Step 2: Convert to retrievers
chapter_retriever = chapter_vs.as_retriever(search_type="similarity", search_kwargs={"k":5})
summary_retriever = summary_vs.as_retriever(search_type="mmr", search_kwargs={"k":5})

# Step 3: Build RetrievalQA chains
chapter_chain = build_retrieval_qa(chapter_retriever)
summary_chain = build_retrieval_qa(summary_retriever)

# Step 4: Run a query
query = "What challenges did Harry face during the Triwizard Tournament?"
print("🔍 From Chapters:\n", chapter_chain.run(query))
print("\n📝 From Summaries:\n", summary_chain.run(query))
