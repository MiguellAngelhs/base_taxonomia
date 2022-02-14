from rest_framework import routers
from extraccion.viewsets import *

urlpatterns =[]
router = routers.SimpleRouter()
router.register('upload', FileZipViewSet, basename='sendUpload')
urlpatterns += router.urls



