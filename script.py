import os
from PyPDF2 import PdfReader,PdfWriter

def process_file(file_name,angle,page_no):
    path='C:/Users/uchih/PdfApp/uploads'+f'/{file_name}'
    #creating two pdf instances to modify our pdf
    pdf_reader=PdfReader(str(path))
    pdf_writer=PdfWriter()

    for pagenum in range(pdf_reader.numPages):  
        page=pdf_reader.getPage(pagenum)
        if pagenum==int(page_no):
            page.rotateClockwise(int(angle))
        pdf_writer.addPage(page)

    save_path="C:/Users/uchih/PdfApp/processed/"
    file_name=file_name[:-4]
    completeName = os.path.join(save_path,f'{file_name}'+'_modified.pdf') 
    file = open(completeName, "wb")
    pdf_writer.write(file)
    file.close()
