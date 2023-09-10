from django.shortcuts import render
from blog.models import Post, CategoriaCarrera

# Create your views here.
def inicio(request):

    profesor = CategoriaCarrera.objects.get(id=1)
    estudiante = CategoriaCarrera.objects.get(id=2)

    post_profesor = Post.objects.filter(categorias = profesor)
    post_estudiante = Post.objects.filter(categorias = estudiante)

    return render(request, "UniversityWebApp/inicio.html", {"post_profesor":post_profesor, "post_estudiante":post_estudiante})

def perfil_usuario(request):

    return render(request, "UniversityWebApp/perfil_usuario.html")