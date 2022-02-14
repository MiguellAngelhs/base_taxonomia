from django.db.models.fields import IntegerField
from rest_framework import serializers
from extraccion.models import *


class ZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadZip
        fields = '__all__'

class TaxonomySerializer(serializers.ModelSerializer ):
    class Meta:
        model = Taxonomia
        fields = '__all__'