from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from perfil_usuario.models import DatosExtra
from validators import *

# Create your views here.
@login_required
def perfil_usuario(request):

    user = User.objects.get(username=request.user)
    tipo_usuario = user.groups.all()

    datos_extra = DatosExtra.objects.get(user=user)

    info_usuario = datos_extra.info_user
    telefono = datos_extra.numero_telefono

    return render(request, "perfil_usuario/perfil_usuario.html", {"tipo_usuario":tipo_usuario, "info_usuario":info_usuario, "telefono":telefono})

@login_required
def editar_perfil(request):

    if request.method == "POST":
        new_username = request.POST.get("username")
        acerca_de = request.POST.get("about")
        telefono = request.POST.get("phone")
        new_email = request.POST.get("email")
        password = request.POST.get("password")

        user = request.user
        password_valida = user.check_password(password)

        characters_error(request, new_username)
        username_existe(request, new_username)
        password_novalida(request, password)
            

        if password_valida and not username_existe:
            user.username = new_username
            user.email = new_email
            user.save()
            
            if password_valida:
                datos_extra, created = DatosExtra.objects.get_or_create(user=user)
                datos_extra.info_user = acerca_de
                datos_extra.numero_telefono = telefono
                datos_extra.save()

    return render(request, "perfil_usuario/editar_perfil.html", {"active_tab":"editar_perfil"})

@login_required
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