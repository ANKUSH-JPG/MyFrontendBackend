from django.db import models


class ExperienceModel(models.Model):
    Company=models.CharField(max_length=50,null=False)
    Position=models.CharField(max_length=100,null=False)
    StartDate=models.DateField()
    EndDate=models.DateField(blank=True)
    Description=models.CharField(max_length=10000,null=False)

    def __str__(self):
        return self.Company

class SkillModel(models.Model):
    Category=models.CharField(max_length=50,null=False)
    Skill=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.Skill
 
class CertificateModel(models.Model):
    Company=models.CharField(max_length=50,null=False)
    Name=models.CharField(max_length=100,null=False)
    StartDate=models.DateField()
    EndDate=models.DateField(blank=True)
    Description=models.CharField(max_length=10000,null=False)

    def __str__(self):
        return self.Name   

class ProjectModel(models.Model):
    Name=models.CharField(max_length=100,null=False)
    StartDate=models.DateField()
    EndDate=models.DateField(blank=True)
    Description=models.CharField(max_length=10000,null=False)
    
    def __str__(self):
        return self.Name