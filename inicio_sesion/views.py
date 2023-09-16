from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("inicio")
        
        else:
            messages.error(request, "La cuenta no existe. Ingrese los datos correctamente")

    return render(request, "inicio_sesion/inicio_sesion.html", {"user":request.user})


def cerrar_sesion(request):
    logout(request)

    return redirect("inicio")