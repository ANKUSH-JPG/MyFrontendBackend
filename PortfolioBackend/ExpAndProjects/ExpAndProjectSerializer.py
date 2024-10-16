from .models import ExperienceModel,SkillModel,ProjectModel,CertificateModel
from rest_framework import serializers

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = "__all__"
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = "__all__"
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = "__all__"
        
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateModel
        fields = "__all__"