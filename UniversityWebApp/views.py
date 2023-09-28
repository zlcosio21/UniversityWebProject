from django.shortcuts import render, redirect
from blog.models import Post, TipoUsuario

# Create your views here.
def inicio(request):

    tipo_usuario_estudiante, created = TipoUsuario.objects.get_or_create(nombre = "Estudiante")
    tipo_usuario_profesor, created = TipoUsuario.objects.get_or_create(nombre = "Profesor")

    tipo_usuario_estudiante = TipoUsuario.objects.get(nombre = "Estudiante")
    tipo_usuario_profesor = TipoUsuario.objects.get(nombre = "Profesor")
    
    post_estudiante = Post.objects.filter(categoria = tipo_usuario_estudiante)
    post_profesor = Post.objects.filter(categoria = tipo_usuario_profesor)
    
    user = request.user

    if not user.is_authenticated:
        return redirect("inicio_sesion")

    return render(request, "UniversityWebApp/inicio.html", {"post_profesor":post_profesor, "post_estudiante":post_estudiante})