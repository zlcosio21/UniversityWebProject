from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(unique=True, max_length=50, null=False)

    class meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'

    def __str__(self):
        return self.nombre