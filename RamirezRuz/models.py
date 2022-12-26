from django.db import models


# Create your models here.

class CarrerasModel(models.Model):
    name=models.CharField(max_length=200)
    cantidad_ano=models.IntegerField()
    cantidad_asignaturas=models.IntegerField()
    
    