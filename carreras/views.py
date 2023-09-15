from django.shortcuts import render, redirect
from carreras.models import Carrera, Materia, Salon, Semestre

# Create your views here.
def matricular_carrera(request, carrera_nombre):
    try:

        carrera = Carrera.objects.get(nombre__iexact=carrera_nombre)
        estudiantes_semestre = Semestre.objects.get(carrera=carrera, numero=1)

        materias_carrera = Materia.objects.filter(semestre__carrera=carrera, semestre__numero=1)
        salones_carrera = Salon.objects.filter(semestre__carrera=carrera, semestre__numero=1)

        user = request.user
        
        carrera_matriculada = user.carreras_matriculadas.filter(id=carrera.id).exists()
        ya_esta_matriculado = user.carreras_matriculadas.exists()
        
        if carrera_matriculada:
            
            return render(request, "carreras/carrera.html", {"carrera_nombre": carrera_nombre, "materias_carrera":materias_carrera, "salones_carrera":salones_carrera})

        elif ya_esta_matriculado:
            return render(request, "carreras/ya_matriculado.html", {"carrera_nombre":carrera_nombre})
        
        else:
            carrera.estudiantes.add(user)
            carrera.save()

            estudiantes_semestre.estudiantes.add(user)
            estudiantes_semestre.save()

            return render(request, "carreras/carrera.html", {"carrera_nombre": carrera_nombre, "materias_carrera":materias_carrera, "salones_carrera":salones_carrera})
        
    except carrera.DoesNotExist:
        return redirect('inicio')
    

def especializarse(request, materia_nombre):
    try:

        materia = Materia.objects.get(nombre__iexact=materia_nombre)
        salones = Salon.objects.filter(materia=materia, profesor=None)
        user = request.user

        materia_especializada = user.salones_profesor.filter(materia=materia).exists()
        ya_especializado = user.salones_profesor.filter(materia=materia).exists()
        
        if materia_especializada:

            salones_profesor = Salon.objects.filter(profesor=user)

            return render(request, "carreras/especializado.html", {"salones_profesor":salones_profesor, "materia":materia})

        elif ya_especializado:
            return render(request, "carreras/ya_especializado.html")
        
        else:

            for salon in salones:
                salon.profesor = user
                salon.save()

            salones_profesor = Salon.objects.filter(profesor=user)

            return render(request, "carreras/especializado.html", {"salones_profesor":salones_profesor, "materia":materia})
        
    except Materia.DoesNotExist:
        return redirect('inicio')