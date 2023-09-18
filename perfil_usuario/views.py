from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def perfil_usuario(request):

    user = User.objects.get(username=request.user)
    tipo_usuario = user.groups.all()

    return render(request, "perfil_usuario/perfil_usuario.html", {"tipo_usuario":tipo_usuario})

def editar_perfil(request):
    
    return render(request, "perfil_usuario/editar_perfil.html", {"active_tab":"editar_perfil"})

def cambiar_password(request):

    if request.method == "POST":
        password_actual = request.POST.get("password")
        password_actual_valida = request.user.check_password(password_actual)

        nueva_password = request.POST.get("new_password")
        nueva_password_confirm = request.POST.get("new_password_confirm")

        user = request.user

        if len(nueva_password) < 8 and len(nueva_password_confirm) < 8:
            messages.error(request, "La contraseña debe tener minimo 8 caracteres", extra_tags="error_characters")
            
        if nueva_password != nueva_password_confirm:
            messages.error(request, "Las contraseñas deben ser iguales. Ingrese nuevamente", extra_tags="password_error")
        
        if not password_actual_valida:
            messages.error(request, "La contraña actual es incorrecta, ingrese nuevamente", extra_tags="password_novalida")
        
        if password_actual_valida and nueva_password == nueva_password_confirm:   
            user.set_password(nueva_password)
            user.save()

            login(request, user)

            return redirect("inicio")

    return render(request, "perfil_usuario/cambiar_password.html")