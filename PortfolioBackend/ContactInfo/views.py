from .models import ContactInfoModel
from .ContactInfoSerializer import ContactInfoSerializer
from rest_framework import viewsets

# Create your views here.

class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfoModel.objects.all()
    serializer_class = ContactInfoSerializer