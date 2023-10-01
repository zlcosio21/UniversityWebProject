from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50, null=True)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.tipo_usuario.nombre == "Estudiante":
            return f"Matricular carrera {self.titulo.capitalize()}"
        else:
            return f"Especializar materia {self.titulo.capitalize()}"