from django.db import models


class Taxonomia(models.Model):
    file = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField()

    def __str__(self) -> str:
        return 'id: %s FILE: %s LEVEL: %s' % (self.id, self.file, self.level)