import re
from langchain.docstore.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_by_chapters(cleaned_text:str)->str:
    """
    split cleaned text based on chapter

    """
    parts=re.split(r'(CHAPTER\s[A-Z]+(?:\s[A-Z]+)*)',cleaned_text)

    documents=[]

    for i in range(1,len(parts),2):
        title=parts[i].strip()
        content=parts[i+1].strip()

        doc=Document(page_content=content,
                     metadata={"chapter_title": title ,"chapter":i//2+1})
        documents.append(doc)
    print('.....chunking.....done....')
    return documents

def chunk_chapter_text(chapter_text:str)->list[Document]:
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    return splitter.create_documents([chapter_text])
