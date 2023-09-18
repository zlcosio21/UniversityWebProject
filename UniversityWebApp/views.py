from django.shortcuts import render, redirect
from blog.models import Post, TipoUsuario

# Create your views here.
def inicio(request):

    estudiante = TipoUsuario.objects.get(id=1)
    profesor = TipoUsuario.objects.get(id=2)
    
    post_profesor = Post.objects.filter(categorias = profesor)
    post_estudiante = Post.objects.filter(categorias = estudiante)
    
    user = request.user

    if not user.is_authenticated:
        return redirect("inicio_sesion")

    return render(request, "UniversityWebApp/inicio.html", {"post_profesor":post_profesor, "post_estudiante":post_estudiante})