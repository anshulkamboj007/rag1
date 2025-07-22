import re


def clean_text(text:str)->str:

    # remove tab 
    text=re.sub(r'\t', ' ',text)

    #remove multiple blank lines 
    text=re.sub(r'\n\s*\n','\n',text)

    # Fix word splits across lines
    text=re.sub(r'(\w)\n(\w)',r'\1\2',text)

    # Remove single newlines (often inside sentences)
    text=text.replace('\n',' ')

    # Collapse multiple spaces
    text=re.sub(r' +',' ',text)

    return text.strip()

if __name__=='__main__':
    from data_ingestion import load_pdf_text
    from variables import PDF_FILE
    raw=load_pdf_text(PDF_FILE)
    cleaned=clean_text(raw)
    print('cleaned text preview')
    print(cleaned[:100])