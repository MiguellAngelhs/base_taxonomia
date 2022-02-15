import zipfile
from zipfile import ZipFile
import os
from extraccion.models import Taxonomia
from extraccion.serializer import *
from extraccion.controllers.utilities import *
from extraccion.controllers.utilities2doc import *
from extraccion.controllers.utilities_image import *
from extraccion.controllers.utilities_audio import *
from dotenv import load_dotenv
load_dotenv()
File = os.getenv('DIR_EXTRACTION')




def estrationFileZip(ruta_zip,ruta_extraccion,password):
        
    archivo_zip = zipfile.ZipFile(ruta_zip, "r")
    try:
        print(archivo_zip.namelist())
        archivo_zip.extractall(pwd=password, path=ruta_extraccion)
    except:
        pass
    archivo_zip.close()

def taxonomy1(file):
    print('**************************************************************************')
    level=0
    name_directory = file.split('/')[-1]
    print(' '*level+' '+str(level)+' '+name_directory)
    file_type ='folder'
    a = Taxonomia.objects
    a.create(file=name_directory, level=level,typefile=file_type, directory='./')
    taxonomy(file,level)


def taxonomy(file, level):
    for i in range(0,1000):
            Files_dir = [file+'/'+archivo for archivo in os.listdir(file+'/') if archivo.endswith("")]
            Files_dir.sort()
    level_dir = level+1
    for k in Files_dir:
        a = Taxonomia.objects
        name_level = k.split('/')[-1]
        name_level_father = k.split('/')[-2]
        directory = k.replace(File, '')
        level_basic = level_dir-2
        if os.path.isdir(k):
            file_type ='folder'
            if level_basic >= 0:
                print(" "*level_dir+' '+str(level_basic)+'.'+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
                n = Taxonomia.objects.filter(file=name_level_father)
                lenfilther = len(n)-1
                level_ftaher =n[lenfilther].id
                a.create(file=name_level, level=level_dir, levelfather = level_ftaher,typefile=file_type, directory='./'+directory)
                taxonomy(k,level_dir)
            else:
                print(" "*level_dir+' '+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
                n = Taxonomia.objects.filter(file=name_level_father)
                lenfilther = len(n)-1
                level_ftaher =n[lenfilther].id
                a.create(file=name_level, level=level_dir, levelfather = level_ftaher,typefile=file_type, directory='./'+directory)
                taxonomy(k,level_dir)

        else:
            extention= name_level.split('.')[-1]
            extention_document = ['doc','docx','pdf']
            extention_imagen = ["bmp", "tiff", "jpeg", "gif", "png", "jpg",
                    "webp", "svg", "tif", "RAW", "psd", "eps", "pic"]
            extention_audio = ['mp3','flac','wav']
            extention_video = ['mp4','flac']
            text=''
            numpages = 0
            number_word=0
            minute = False

            if extention in extention_document:
                file_type = 'Document'
                if (extention=='pdf'):
                    text = get_pdf_searchable_pages(k)
                    numpages = getnumberpages(k)
                    number_word = len(text.split())
                elif (extention == "doc" or extention == "docx"):
                    text = doc2text(k)
                    numpages =numpagesdoc(text)
                    number_word = len(text.split())
            elif extention in extention_imagen:
                file_type = 'Imagen'
                text=image2text(k)
                number_word = len(text.split())

            elif extention in extention_audio:
                file_type = 'Audio'
                text,array,minute = apiAudio(k)
                number_word = len(text.split())
                
            elif extention in extention_video:
                file_type = 'Video'
                text,array,minute = apiAudio(k)
                number_word = len(text.split())
                
            else:
                file_type = 'Other file'
            
            if level_basic >= 0:
                print(" "*level_dir+' '+str(level_basic)+'.'+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
                n = Taxonomia.objects.filter(file=name_level_father)
                lenfilther = len(n)-1
                level_ftaher =n[lenfilther].id
                a.create(file=name_level, level=level_dir, levelfather = level_ftaher,
                typefile=file_type, directory='./'+directory,numpages = numpages, 
                transcription = text, numwords = number_word)
                if minute is True:
                    idfull = Taxonomia.objects.last().id
                    mintomin(array, int(idfull))

            else:
                print(" "*level_dir+' '+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
                n = Taxonomia.objects.filter(file=name_level_father)
                lenfilther = len(n)-1
                level_ftaher =n[lenfilther].id
                a.create(file=name_level, level=level_dir, levelfather = level_ftaher,
                typefile=file_type, directory='./'+directory,numpages = numpages, 
                transcription = text, numwords = number_word)
                if minute is True:
                    idfull = Taxonomia.objects.last().id
                    mintomin(array, int(idfull))



