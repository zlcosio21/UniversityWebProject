from django.shortcuts import render
from blog.models import Post

# Create your views here.
def inicio(request):

    posts = Post.objects.all()

    return render(request, "UniversityWebApp/inicio.html", {"posts":posts})

def perfil_usuario(request):

    return render(request, "UniversityWebApp/perfil_usuario.html")