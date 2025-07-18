from data_ingestion import load_pdf_text
from data_cleaning import clean_text
from variables import PDF_FILE,DATA_FOLDER

text = load_pdf_text(PDF_FILE)
cleantext=clean_text(text)

print(cleantext[:100])