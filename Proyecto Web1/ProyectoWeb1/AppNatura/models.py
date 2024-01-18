from django.db import models

# Create your models here.
class Productos(models.Model):
    
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)

    class Meta:
        app_label = 'AppNatura'

class Perfume(models.Model):

    nombre = models.CharField(max_length=50)
    contenido_neto = models.IntegerField()
    vto = models.DateField()
    precio = models.FloatField()

class CremaCorporal(models.Model):

    nombre = models.CharField(max_length=50)
    contenido_neto = models.IntegerField()
    vto = models.DateField()
    precio = models.FloatField()



