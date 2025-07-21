from llm_chain import get_llm
from langchain.chains import RetrievalQA

def build_retrieval_qa(retriever, return_sources=True):
    llm = get_llm
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=return_sources
    )
