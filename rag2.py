from vector_store import load_or_create_vectorstore
from variables import PDF_FILE,DATA_FOLDER

vectorstore = load_or_create_vectorstore(PDF_FILE)
retriever = vectorstore.as_retriever()