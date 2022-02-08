import zipfile
from zipfile import ZipFile
import os




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
    taxonomy(ruta_extraccion+foldername,level)


def taxonomy(file, level):
    for i in range(0,1000):
            Files_dir = [file+'/'+archivo for archivo in os.listdir(file+'/') if archivo.endswith("")]
            Files_dir.sort()
    level_dir = level+1
    #print(Files_dir, 'este es el primer nivel')
    for k in Files_dir:
        name_level = k.split('/')[-1]
        level_basic = level_dir-2
        if os.path.isdir(k):
            #print(os.path.isdir(k))
            #name_level = k.split('/')[-1]
            if level_basic >= 0:
                print(" "*level_dir+' '+str(level_basic)+'.'+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
                taxonomy(k,level_dir)
            else:
                print(" "*level_dir+' '+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
                taxonomy(k,level_dir)

        else:
            if level_basic >= 0:
                print(" "*level_dir+' '+str(level_basic)+'.'+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)
            else:
                print(" "*level_dir+' '+str(level_dir-1)+'.'+str(level_dir)+' '+name_level)

if __name__ == "__main__":
    directory_zip = "/home/mahs/Escritorio/DEV/base_taxonomia/FileZip/"
    ruta_zip = directory_zip+"libsndfile.zip"
    ruta_extraccion = "/home/mahs/Escritorio/DEV/base_taxonomia/UnFileZip/"
    password = None
    name=ruta_zip.split('/')[-1]
    foldername = name.split('.')[0]
    estrationFileZip(ruta_zip,ruta_extraccion,password)
    taxonomy1(ruta_extraccion+foldername)