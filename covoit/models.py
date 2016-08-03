from django.db import models

# Create your models here.
class TypeOffre(models.Model):
    libelle=models.CharField(max_length=200)
   
    def __str__(self):
        return self.libelle