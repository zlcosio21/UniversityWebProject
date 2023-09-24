from django.contrib import messages
from django.contrib.auth.models import User

def characters_error(request, *args):
    for var in args:
        if len(var) < 8:
            messages.error(request, "Debe contener minimo 8 caracteres", extra_tags="characters_error")

def username_existe(request, new_username):
    user = request.user
    existe = User.objects.filter(username=new_username).exclude(pk=user.pk).exists()

    if existe:
        return messages.error(request, "El nuevo nombre de usuario ya está en uso.", extra_tags="username_existe_error")

def password_novalida(request, password_actual):
    user = request.user

    password_valida = user.check_password(password_actual)
    if not password_valida:
        return messages.error(request, "La contraseña actual es incorrecta, ingrese nuevamente", extra_tags="password_novalida")
    
def equals_error(request, password, password_confirm):

    if password != password_confirm:
        return messages.error(request, "Las contraseñas deben ser iguales. Ingrese nuevamente", extra_tags="password_error")