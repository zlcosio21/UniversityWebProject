from django.shortcuts import render

# Create your views here.
def perfil_usuario(request):

    return render(request, "perfil_usuario/perfil_usuario.html")