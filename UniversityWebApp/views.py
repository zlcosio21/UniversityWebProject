from django.shortcuts import render
from blog.models import Post, TipoUsuario
from carreras.models import Carrera

# Create your views here.
def inicio(request):
    carreras = Carrera.objects.all()
    lista_carreras = []

    for carrera in carreras:
        lista_carreras.append(carrera.nombre)

    estudiante = TipoUsuario.objects.get(id=1)
    profesor = TipoUsuario.objects.get(id=2)
    
    post_profesor = Post.objects.filter(categorias = profesor)
    post_estudiante = Post.objects.filter(categorias = estudiante)

    return render(request, "UniversityWebApp/inicio.html", {"post_profesor":post_profesor, "post_estudiante":post_estudiante, "lista_carreras":lista_carreras})

def perfil_usuario(request):

    return render(request, "UniversityWebApp/perfil_usuario.html")