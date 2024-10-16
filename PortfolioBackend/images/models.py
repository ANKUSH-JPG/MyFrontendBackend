from django.db import models

class images(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Url=models.CharField(max_length=200,null=False)
    
    def __str__(self):
        return self.Name
