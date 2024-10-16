from rest_framework import viewsets
from .models import ExperienceModel,SkillModel,ProjectModel,CertificateModel
from .ExpAndProjectSerializer import ExperienceSerializer,SkillSerializer,ProjectSerializer,CertificateSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer
    
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
    

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = CertificateModel.objects.all()
    serializer_class = CertificateSerializer