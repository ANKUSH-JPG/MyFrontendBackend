from django.db import models

# Create your models here.


class ContactInfoModel(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=254,unique=True,null=False)
    PhoneNo=models.CharField(max_length=20,unique=True,null=False)
    Address=models.CharField(max_length=254,null=False)
    Linkedin=models.CharField(max_length=20,unique=True,null=False)
    Github=models.CharField(max_length=50,unique=True,null=False)
    Naukri=models.CharField(max_length=50,unique=True,null=False)
    Indeed=models.CharField(max_length=50,unique=True,null=False)
        
    def __str__(self):
        return self.Name