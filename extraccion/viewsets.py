
import os
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from extraccion.models import *
from extraccion.serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import Response
from extraccion.controllers.ExtartionZip import *


from dotenv import load_dotenv
load_dotenv()
PROJECT_PATH = os.getenv("FILEZIP")
#site.addsitedir(PROJECT_PATH)

load_dotenv()
File = os.getenv('DIR_EXTRACTION')
#site.addsitedir(File)


class FileZipViewSet(viewsets.ModelViewSet):
    queryset = UploadZip.objects.all()
    serializer_class = ZipSerializer
    
    #parser_classes = (JSONParser, MultiPartParser, FormParser)

    #@csrf_exempt
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
          
        name = str(request.data['link'])
        print(name)
    
        if serializer.is_valid():
            serializer.save()
            directory_zip = PROJECT_PATH
            ruta_zip = directory_zip+name
            print(ruta_zip)
            print(File)
            ruta_extraccion = File
            password = None 
            estrationFileZip(ruta_zip,ruta_extraccion,password)
            namefol=ruta_zip.split('/')[-1]
            foldername = namefol.split('.')[0]
            print(ruta_extraccion+foldername)
            taxonomy1(ruta_extraccion+foldername)
            return Response(serializer.data)
        return Response(serializer.errors)