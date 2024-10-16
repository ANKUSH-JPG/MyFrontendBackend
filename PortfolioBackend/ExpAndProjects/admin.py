from django.contrib import admin
from .models import ExperienceModel,SkillModel,ProjectModel,CertificateModel

# Register your models here.
admin.site.register(ExperienceModel)
admin.site.register(SkillModel)
admin.site.register(ProjectModel)
admin.site.register(CertificateModel)