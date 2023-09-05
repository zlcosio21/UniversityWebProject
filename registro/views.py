from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.db.utils import IntegrityError

# Create your views here.
def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        tipo_usuario = request.POST.get("tipo_usuario")

        if password == password_confirm:

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                if tipo_usuario == "estudiante":
                    group = Group.objects.get(name="Estudiantes")
                else:
                    group = Group.objects.get(name="Profesores")

                user.groups.add(group)

            except IntegrityError:
                redirect("inicio")    

            return redirect("inicio")

        else:
            return redirect("inicio")

    return render(request, "registro/registro.html")