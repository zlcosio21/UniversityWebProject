from django.shortcuts import render

# Create your views here.
def inicio(request):

    return render(request, "UniversityWebApp/inicio.html")

def registro(request):

    return render(request, "UniversityWebApp/registro.html")

def inicio_sesion(request):

    return render(request, "UniversityWebApp/inicio_sesion.html")

def perfil_usuario(request):

    return render(request, "UniversityWebApp/perfil_usuario.html")