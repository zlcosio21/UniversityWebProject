from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(unique=True, max_length=50, null=False)
    estudiantes = models.ManyToManyField(User, related_name='carreras_matriculadas', blank=True, limit_choices_to={'groups__name': 'Estudiante'})

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Semestre(models.Model):
    numero = models.PositiveIntegerField()
    estudiantes = models.ManyToManyField(User, related_name='semestre_estudiantes', blank=True, limit_choices_to={'groups__name': 'Estudiante'})
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.carrera.nombre} - Semestre {self.numero}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"
    

class Salon(models.Model):
    nombre = models.CharField(max_length=50, unique=True, null=False)
    estudiantes = models.ManyToManyField(User, related_name='salones_estudiantes', blank=True, limit_choices_to={'groups__name': 'Estudiante'})
    profesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='salones_profesor', blank=True, limit_choices_to={'groups__name': 'Profesor'})
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=False, default=1)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, null=False)
    imagen = models.ImageField(upload_to='salones', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'salon'
        verbose_name_plural = 'salones'

    def __str__(self):
        return f"Salon {self.nombre} - Materia {self.materia.nombre} - Carrera {self.semestre.carrera.nombre} - Semestre {self.semestre.numero} - Profesor {self.profesor}"