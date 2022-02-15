from django.db import models


class UploadZip(models.Model):
    link = models.FileField(upload_to='FileZip/', null=True, blank=True)

    def __str__(self) -> str:
        return 'id: %s link: %s' % (self.id, self.link)


class Taxonomia(models.Model):

    file = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField()
    levelfather = models.IntegerField(null=True, blank=True)
    typefile = models.CharField(max_length=50, null=True, blank=True)
    directory = models.CharField(max_length=500, null=True, blank=True)
    numpages =  models.IntegerField(null=True, blank=True)
    transcription = models.TextField(null=True, blank=True)
    numwords =  models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return 'id: %s FILE: %s LEVEL: %s LEVEL_FATHER: %s' % (self.id, self.file, self.level, self.levelfather)

    '''modelo para la transcripción de minuto a minuto de los audios y videos'''
class MinuteToMinute(models.Model):
    fileId = models.ForeignKey(Taxonomia, on_delete=models.CASCADE)
    minuteAudio = models.IntegerField(blank=True)
    sourceText = models.TextField(blank=True)
    finalText = models.TextField(blank=True)

    def __str__(self) -> str:
        return 'id: %s  minuteAudio' % (self.fileId, self.minuteAudio)