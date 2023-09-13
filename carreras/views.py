from django.shortcuts import render, redirect
from carreras.models import Carrera, Materia

# Create your views here.
def matricular_carrera(request, carrera_nombre):
    try:

        carrera = Carrera.objects.get(nombre__iexact=carrera_nombre)
        materias_carrera = Materia.objects.filter(materia_perteneciente_a__carrera=carrera)

        user = request.user
        
        carrera_matriculada = user.carreras_matriculadas.filter(id=carrera.id).exists()
        ya_esta_matriculado = user.carreras_matriculadas.exists()
        
        if carrera_matriculada:
            carrera.estudiantes.add(user)
            carrera.save()

            return render(request, "carreras/carrera.html", {"carrera_nombre": carrera_nombre, "materias_carrera":materias_carrera})

        elif ya_esta_matriculado:
            return render(request, "carreras/ya_matriculado.html", {"carrera_nombre":carrera_nombre})
        
        else:
            carrera.estudiantes.add(user)
            carrera.save()

            return render(request, "carreras/carrera.html", {"carrera_nombre": carrera_nombre, "materias_carrera":materias_carrera})
        
    except carrera.DoesNotExist:
        return redirect('inicio')