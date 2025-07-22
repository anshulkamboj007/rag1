# rag2.py

from vectorstore.vector_manager import VectorStoreManager
from llm_chain import summarize_func, get_llm
from retriver import build_retrieval_qa

# Step 1: Get vectorstores
print ('Step 1: Get vectorstores :  ..started.....')
vs_manager = VectorStoreManager()
chapter_vs = vs_manager.get_chapter_vectorstore()
print ('Step 1: Get vectorstores :  ..chapter_vs completed.....')
summary_vs = vs_manager.get_summary_vectorstore(summarize_func)
print ('Step 1: Get vectorstores :  ..summary_vs completed.....')

# Step 2: Convert to retrievers
print ('Step 2: Convert to retrievers  ..started.....')
chapter_retriever = chapter_vs.as_retriever(search_type="similarity", search_kwargs={"k":2})
summary_retriever = summary_vs.as_retriever(search_type="mmr", search_kwargs={"k":2})
print ('Step 2: Convert to retrievers  ..completed.....')

# Step 3: Build RetrievalQA chains
print ('Step 3: Build RetrievalQA chains  ..started.....')
chapter_chain = build_retrieval_qa(chapter_retriever)
summary_chain = build_retrieval_qa(summary_retriever)
print ('Step 3: Build RetrievalQA chains  ..completed.....')

# Step 4: Run a query
print ('Step 4: Run a query  ..started.....')
query = "who are the friends of harry ?"
print("🔍 From Chapters:\n", chapter_chain.invoke(query))

print(f'----summariy of top chapter----- \n')
print("\n📝 From Summaries:\n", summary_chain.invoke(query))
