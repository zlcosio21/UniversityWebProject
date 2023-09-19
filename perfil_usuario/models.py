from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info_user = models.CharField(max_length=500, null=True)
    img_perfil = models.ImageField(upload_to='perfil_usuario', null=True)
    numero_telefono = models.CharField(max_length=20, null=True)

    class meta:
        verbose_name = 'datos_extra'
        verbose_name_plural = 'datos_extras'

    def __str__(self):
        return f" Datos extras del user {self.user}"