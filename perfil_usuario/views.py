from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def perfil_usuario(request):

    user = User.objects.get(username=request.user)
    tipo_usuario = user.groups.all()

    return render(request, "perfil_usuario/perfil_usuario.html", {"tipo_usuario":tipo_usuario})

def editar_perfil(request):
    
    return render(request, "perfil_usuario/editar_perfil.html", {"active_tab":"editar_perfil"})

def cambiar_password(request):

    return render(request, "perfil_usuario/cambiar_password.html")