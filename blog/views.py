from django.shortcuts import render
from blog.models import Post, TipoUsuario

# Create your views here.
def categoria(request, categoria_id):
    
    categoria = TipoUsuario.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)

    return render(request, "blog/categoria.html", {"categoria":categoria, "posts":posts})