from .imageSerializer import ImageSerializer
from .models import images
from rest_framework import viewsets

class ImageModelView(viewsets.ModelViewSet):
    queryset = images.objects.all()
    serializer_class = ImageSerializer