from extraccion.controllers.speechToText import *
from extraccion.models import *
from extraccion.serializer import *


def apiAudio(path):
    ruta = (path)
    sound = AudioSegment.from_file(ruta)
    soundMono = sound.set_channels(1)
    timeSound = len(soundMono)
    time = timeSound
    sizeAudio = time/60000
    sizeList = math.ceil(sizeAudio)
    audio = Cositas(ruta, sizeList)
    transcription, arrayTranscription = audio.proces()

    return transcription, arrayTranscription,True

def mintomin(array, id_full):
    for i in range(len(array)):
        textDB = MinuteToMinute(fileId=Taxonomia.objects.filter(id=id_full)[0],
                                minuteAudio=i, sourceText=array[i])
        textDB.save()
    