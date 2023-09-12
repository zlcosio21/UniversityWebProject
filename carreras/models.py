from django.db import models

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
    
class Materia(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    carrera = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    
    class meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'

    def __str__(self):
        return f"{self.nombre} - Carrera {self.carrera.carrera.nombre} - Semestre {self.carrera.numero}"