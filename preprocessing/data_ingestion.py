import PyPDF2
import os
from variables import DATA_FOLDER,PDF_FILE

def load_pdf_text(filename:str)->str:
    dir_path=os.path.join(os.path.dirname(__file__),'data')
    pdf_path=os.path.join(dir_path,filename)

    print(f'loading pdf from path : {pdf_path}')

    with open(pdf_path,'rb') as f:
        reader =PyPDF2.PdfReader(f) 
        full_text=' '.join([page.extract_text() for page in reader.pages])
    return full_text

if __name__ =='__main__':
    raw_text=load_pdf_text(PDF_FILE)
    print(raw_text[:200])



