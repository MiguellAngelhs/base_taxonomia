from ast import Not
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
from pdf2image import convert_from_path
import os
import pytesseract
import shutil
from tika import parser
from PyPDF2 import PdfFileReader
import fitz
from pdfminer.pdfpage import PDFPage
from dotenv import load_dotenv
load_dotenv()
pathcreated = os.getenv('DIR_TRANCRIPTION')


def validatepdf(path):
    new_path = path.split('/')[-1]
    name=new_path.split('.')[0]
    directorio = pathcreated+name 
    try:
        os.mkdir(directorio)
    except OSError:
        pass
        #print("La creación del directorio %s falló" % directorio)
    else:
        pass
        #print("Se ha creado el directorio: %s " % directorio)
    #open the fitz file
    pdf = fitz.open(path)

    #select the page number
    image_list = pdf.getPageImageList(0)

    #applying the loop
    for image in image_list:
        xref = image[0]
        pix = fitz.Pixmap(pdf, xref)
        if pix.n < 5:
            pix.writePNG(pathcreated+name+'/'+f'{xref}.png')
        else:
            pix1 = fitz.open(fitz.csRGB, pix)
            pix1.writePNG(pathcreated+name+'/'+f'{xref}.png')
            pix1 = None
        pix = None
    return image_list

def get_pdf_searchable_pages(path):
    new_path = path.split('/')[-1]
    name=new_path.split('.')[0]
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0
    with open(path, 'rb') as infile:

        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                searchable_pages.append(page_num)
            else:
                non_searchable_pages.append(page_num)
    if page_num > 0:
        if len(searchable_pages) == 0:            
            # print(f"Document '{path}' has {page_num} page(s). "
            #       f"Complete document is non-searchable")
            text = text_of_pdf_nonsearchable(path)
            return text
            
        elif len(non_searchable_pages) == 0:
            # print(f"Document '{path}' has {page_num} page(s). "
            #       f"Complete document is searchable")
            imagenes = validatepdf(path)
            if (len(imagenes)>0 and page_num ==len(imagenes)):
                text=text_of_pdf_nonsearchable(path)
                
                return text
            else:
                text = pdf2text(path)
                #print(text)
                return text
            
        else:                
            # print(f"searchable_pages : {searchable_pages}")
            # print(f"non_searchable_pages : {non_searchable_pages}")
            text = text_of_pdf_nonsearchable(path)
            return text
    else:
        print(f"Not a valid document")



def text_of_pdf_nonsearchable(path):
    new_path = path.split('/')[-1]
    name=new_path.split('.')[0]
    directorio = pathcreated+name 
    try:
        os.mkdir(directorio)
    except OSError:
        pass
        #print("La creación del directorio %s falló" % directorio)
    else:
        pass
        #print("Se ha creado el directorio: %s " % directorio)
    pages = convert_from_path(path, 350)
    i = 1
    for page in pages:
        image_name = pathcreated+name+"/Page_" + str(i) + ".jpeg"  
        page.save(image_name, "JPEG")
        i = i+1 

    for i in range(0,7): 
                    imagenes_png = [archivo for archivo in os.listdir(pathcreated+name) if archivo.endswith(".jpeg")]
                    imagenes_png.sort() 
    #print(imagenes_png)
    text =''
    for img in imagenes_png:
        text += pytesseract.image_to_string(pathcreated+name+'/'+img) # extract text
    replacements = (
        ("6", "ó"),
        ("ion", "ión"),
        ("é","ó"),
        ("dn", "ón"),
        ("ria", "ría"),
        ("ii", "ió"),
        ("io", "ió"),

    )
    text_new =text
    for a, b in replacements:
        text_new = text_new.replace(a, b).replace(a.upper(), b.upper())
    
    try:
        shutil.rmtree(pathcreated+name)
    except OSError as e:
        print(f"Error:{ e.strerror}")
    return text_new


def pdf2text(path):
    new_path = path.split('/')[-1]
    name=new_path.split('.')[0]
    try:
        shutil.rmtree(pathcreated+name)
    except OSError as e:
        print(f"Error:{ e.strerror}")
    text = ""
    #path = '/home/alexander/Escritorio/Base_Product/PruebaZip/pdfnotsearchable/gaceta_07.pdf'
    file_data = parser.from_file(path)
    text = file_data['content']
    # if not text:
    #     text=text_of_pdf_nonsearchable(path)
    #     return text
        
    # else:
    return text
    
def getnumberpages(path):
    a = PdfFileReader(path)
    num_pages = a.getNumPages()
    return num_pages


