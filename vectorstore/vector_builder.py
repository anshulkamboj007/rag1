from langchain_community.vectorstores import FAISS

def build_vectorstore_from_docs(docs, embed_model, path):
    vs = FAISS.from_documents(docs, embed_model)
    vs.save_local(path)
    return vs
