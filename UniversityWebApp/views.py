from django.shortcuts import render

# Create your views here.
def inicio(request):

    return render(request, "UniversityWebApp/inicio.html")

def registro(request):

    return render(request, "UniversityWebApp/registro.html")