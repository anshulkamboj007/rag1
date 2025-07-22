from langchain_core.documents import Document

def summarize_chapters(chapters, summarize_func):
    summarized = []
    for i, doc in enumerate(chapters):
        summary = summarize_func(doc.page_content)
        if summary.strip():
            summarized.append(Document(page_content=summary, metadata=doc.metadata))
    return summarized
