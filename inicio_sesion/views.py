from django.shortcuts import render

# Create your views here.
def inicio_sesion(request):

    return render(request, "inicio_sesion/inicio_sesion.html")