from django.db import models

# Create your models here.
class CategoriaCarrera(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'categoria_carrera'
        verbose_name_plural = 'categorias_carreras'

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)

    categorias = models.ManyToManyField(CategoriaCarrera)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo