from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(unique=True, max_length=50, null=False)

    class meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'

    def __str__(self):
        return self.nombre
    
class Semestre(models.Model):
    numero = models.PositiveIntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.carrera.nombre} - Semestre {self.numero}"