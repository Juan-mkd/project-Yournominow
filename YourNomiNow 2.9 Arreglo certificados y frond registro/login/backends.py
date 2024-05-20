from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from usuario.models import Usuario

class CedulaBackend(BaseBackend):
    def authenticate(self, request, cedula=None, password=None):
        try:
            usuario = Usuario.objects.get(cedula=cedula)
            if check_password(password, usuario.password):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
