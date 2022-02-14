import docx
from docx import Document


'''Api controlador para extraer la transcripción documentos tipo doc y docx'''

'''Función para cambiar el nombre de los archivos con caracteres especiales y llamado de función 
de extraer texto e insercción transcripción de los archivos de la categoría documento de extensión doc y docx'''
def doc2text(path):
    text1=readtxt1(path)
    return text1
    #print(text1)
def numpagesdoc(text1):
    total_line_count = sum(1 for line in text1)
    num_pag = total_line_count/44
    numPag = int(num_pag/44)
    if numPag < 1:
        number_pages = 1
    elif numPag > 1:
        number_pages = numPag + 1
    return number_pages
    
'''función para extarer texto para la transcripción de los documentos de extensión doc y docx'''
def readtxt1(do):
    doc = docx.Document(do)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

