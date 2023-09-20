from django.contrib import messages
from django.contrib.auth.models import User

def characters_error(request, variable):
    if len(variable) < 8:
        messages.error(request, "Debe contener minimo 8 caracteres", extra_tags="username_error")

def username_existe(request, new_username):
    user = request.user
    User.objects.filter(username=new_username).exclude(pk=user.pk).exists()

    return messages.error(request, "El nuevo nombre de usuario ya está en uso.", extra_tags="username_existe_error")

def password_novalida(request, password_actual):
    user = request.user

    password_valida = user.check_password(password_actual)
    if not password_valida:
        return messages.error(request, "La contraña actual es incorrecta, ingrese nuevamente", extra_tags="password_novalida")