from langchain_community.vectorstores import FAISS

def load_vectorstore(path, embed_model):
    return FAISS.load_local(path, embeddings=embed_model, allow_dangerous_deserialization=True)
