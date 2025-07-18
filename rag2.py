from data_ingestion import load_pdf_text
from data_cleaning import clean_text
from data_chunking import split_by_chapters
from variables import PDF_FILE,DATA_FOLDER


raw_text = load_pdf_text(PDF_FILE)
cleaned_text = clean_text(raw_text)
chapter_docs = split_by_chapters(cleaned_text)

print(f"Extracted {len(chapter_docs)} chapters.")
print(chapter_docs[0].metadata)
print(chapter_docs[0].page_content[:500])