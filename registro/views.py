from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib import messages
from validators import *

# Create your views here.
def registro(request):
    grupo_estudiante, created = Group.objects.get_or_create(name = "Estudiante")
    grupo_profesor, created = Group.objects.get_or_create(name = "Profesor")

    grupo_estudiante = Group.objects.get(name ="Estudiante")
    grupo_profesor = Group.objects.get(name = "Profesor")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        tipo_usuario = request.POST.get("tipo_usuario")

        username_characters_error(request, username)
        characters_error(request, password, password_confirm)
        username_existe(request, username)
        equals_error(request, password, password_confirm)

        existe = User.objects.filter(username=username).exclude(pk=user.pk).exists()

        if len(username) >= 8  and (password == password_confirm and len(password) >= 8 and len(password_confirm) >= 8) and existe:

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            if tipo_usuario == "estudiante":
                group = Group.objects.get(name="Estudiante")
            else:
                group = Group.objects.get(name="Profesor")

            user.groups.add(group)    
            login(request, user)

            return redirect("inicio")             

    return render(request, "registro/registro.html", {'messages': messages.get_messages(request)})