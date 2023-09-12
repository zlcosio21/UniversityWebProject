from django.db.models.signals import post_save
from django.dispatch import receiver
from carreras.models import Carrera, Semestre

@receiver(post_save, sender=Carrera)
def crear_semestres(sender, instance, created, **kwargs):
    if created:
        for i in range(1, 11):
            num_semestre = i
            Semestre.objects.create(numero=num_semestre, carrera=instance)