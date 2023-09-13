from django.shortcuts import render, redirect
from carreras.models import Carrera

# Create your views here.
def matricular_carrera(request, carrera_nombre):
    try:
        carrera = Carrera.objects.get(nombre__iexact=carrera_nombre)

        carrera.estudiantes.add(request.user)
        carrera.save()

        return redirect('perfil_usuario')
        
    except carrera.DoesNotExist:
        return redirect('inicio')