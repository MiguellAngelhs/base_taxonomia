import os
from pydub import AudioSegment
from dotenv import load_dotenv
from google.cloud import storage
from google.cloud import speech
import logging
import inspect
import math
from os import remove
class Cositas():
    def __init__(self, pathFile, sizeAudio):
        load_dotenv()
        self.rootPath = os.getenv("DIR_EXTRACTION")
        os.system(f'export GOOGLE_APPLICATION_CREDENTIALS={os.getenv("GOOGLE_APPLICATION_CREDENTIALS")}')
        self.bucketName = os.getenv("BUCKET_NAME")
        self.file =pathFile
        self.size = sizeAudio
        self.name = self.file.split("/")[-1].split(".")[:-1][0]
        self.uri = ""
    

    def proces(self):
        self.convert()
        self.uploadFile()
        texto, listText = self.SpeechToText()
        os.system("unset GOOGLE_APPLICATION_CREDENTIALS")
        return texto, listText


        
    def SpeechToText(self):
        transcripcion = ""
        oraciones = dict()
        time = 0
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=self.uri)
        config = speech.RecognitionConfig(
            encoding='FLAC',
            enable_automatic_punctuation = False,
            enable_word_time_offsets = True,
            language_code = "es-CO",
            audio_channel_count= 2
            
        )
        response = client.long_running_recognize(config=config, audio=audio)
        data = response.result(timeout=600000)
        
        listOracionMinute= [] 
        for _ in range(int(self.size)):
            listOracionMinute.append(' ')
        for b in data.results:
            oracionMinute=""
            transcripcion = transcripcion + b.alternatives[0].transcript
            alternative = b.alternatives[0]
            oracion = b.alternatives[0].transcript
            for word_info in alternative.words:
                word = word_info.word
                end_time = word_info.end_time
                start_time = word_info.start_time
                listOracionMinute[int(math.floor(start_time.total_seconds()/60))] = listOracionMinute[int(math.floor(start_time.total_seconds()/60))]  + str(word) + " "

        return transcripcion,listOracionMinute


    def uploadFile(self):
        cliente = storage.Client()
        bucket  = cliente.bucket(self.bucketName)
        fileName = self.file.split("/")[-1]
        blob = bucket.blob(fileName)
        blob.upload_from_filename(self.file)
        self.uri = f"gs://{self.bucketName}/{fileName}"
        remove(self.file) #eliminamos el archivo .flac y solo dejamos el mp3

    def convert(self):
        audioChannel= " "
        aux = self.file.split("/")[:-1]
        ruta = "/".join(aux)
        audioChannel= " "
        aux = self.file
        sound = AudioSegment.from_file(aux)
        flac=".flac"
        newPath=(self.rootPath + "convert/")
        pathAudio=sound.export(f"{newPath}{self.name}{flac}", format="flac")
        self.file = pathAudio.name