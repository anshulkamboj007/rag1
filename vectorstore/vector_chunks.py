from data_chunking import chunk_chapter_text

def chunk_documents(docs):
    chunked = []
    for doc in docs:
        chunks = chunk_chapter_text(doc.page_content)
        for chunk in chunks:
            chunk.metadata = doc.metadata
        chunked.extend(chunks)
    return chunked
