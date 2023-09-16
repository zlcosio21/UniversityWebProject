from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        tipo_usuario = request.POST.get("tipo_usuario")

        if len(username) < 8:
            messages.error(request, "Debe contener minimo 8 caracteres", extra_tags="username_error")

        if password != password_confirm:     
            messages.error(request, "Las contraseñas deben ser iguales. Ingrese nuevamente", extra_tags="password_error")

        if len(password) < 8 and len(password_confirm) < 8:
            messages.error(request, "La contraseña debe tener minimo 8 caracteres", extra_tags="error_characters")


        if len(username) >= 8  and password == password_confirm:

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