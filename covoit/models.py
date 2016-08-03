from django.db import models

# Create your models here.
class TypeOffre(models.Model):
    libelle=models.CharField(max_length=200)
   
    def __str__(self):
        return self.libelle

class Lieu(models.Model):
    libelle=models.CharField(max_length=50)
    
    def __str__(self):
        return self.libelle
    
class Jour(models.Model):
    libelle=models.CharField(max_length=10)
    
    def __str__(self):
        return self.libelle
    
class OffrePermanente(models.Model):
    lieu=models.ForeignKey(Lieu)
    type=models.ForeignKey(TypeOffre)
    jour=models.ForeignKey(Jour)
    
        
    def isDepart(self):
        return (self.type.libelle == "Départ")
    
    def __str__(self):
        res = "permanent à Xh le " + str(self.jour)
    
        if self.isDepart() :
            res = res + " de " 
        else :
            res = res + " pour "
        
        return res + str(self.lieu)
