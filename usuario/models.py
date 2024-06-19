from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth.hashers import make_password
# Create your models here.

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.rol_nombre

class Cargo(models.Model):
    cargo_id = models.AutoField(primary_key=True)
    cargo_nombre = models.CharField(max_length=200)
    cargo_sueldo_basico = models.IntegerField()
    cargo_empresa = models.CharField(max_length=200)

    def __str__(self):
        return self.cargo_nombre

class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(unique=True)
    usu_nombre = models.CharField(max_length=200)
    usu_correo = models.CharField(max_length=200)
    usu_telefono = models.IntegerField()
    password = models.CharField(max_length=200)
    usu_direccion = models.CharField(max_length=200)
    usu_fecha_ingreso = models.DateTimeField(auto_now_add=True)
    usu_estado = models.CharField(max_length=200, default='activo')
    usu_id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    usu_id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    last_login = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return self.usu_nombre
    
    def is_authenticated(self):
        # Verificar si last_login está dentro de un tiempo aceptable
        if self.last_login is not None:
            # Definir el tiempo máximo de inactividad permitido, por ejemplo, 30 días
            max_inactive_time = timedelta(days=80)
            # Calcular el tiempo transcurrido desde el último inicio de sesión
            elapsed_time = timezone.now() - self.last_login
            # Comprobar si el tiempo transcurrido es menor que el tiempo máximo de inactividad permitido
            return elapsed_time < max_inactive_time
        else:
            # Si last_login es None, el usuario nunca ha iniciado sesión, por lo que no está autenticado
            return False
    
    @classmethod
    def get_email_field_name(cls):
        return 'usu_correo'

password= 'yournomi1033'
@receiver(post_migrate)
def insertRol(sender, **kwargs):
    if kwargs.get('app_config'):
        app_name= kwargs['app_config'].name
        if app_name == 'usuario':
            Rol.objects.bulk_create([
                Rol(rol_id="1", rol_nombre="Administrador"),
                Rol(rol_id="2", rol_nombre="Empleado")
        ])
            Cargo.objects.bulk_create([
                Cargo(cargo_nombre="Gerente", cargo_sueldo_basico="2000000", cargo_empresa="YourNomiNow"),
                Cargo(cargo_nombre="Ceo", cargo_sueldo_basico="3000000", cargo_empresa="YourNomiNow"),
                Cargo(cargo_nombre="Junior", cargo_sueldo_basico="1300000", cargo_empresa="YourNomiNow"),
                Cargo(cargo_nombre="Senior", cargo_sueldo_basico="5000000", cargo_empresa="YourNomiNow")
        ])
            Usuario.objects.bulk_create([
                Usuario(usu_id='1', cedula='123', usu_nombre='admin', usu_correo='nicolasmartinezf137@gmail.com', usu_telefono='123123', password=make_password(password), usu_direccion='calle 123', usu_fecha_ingreso="2024/03/28", usu_estado='activo', usu_id_cargo=Cargo.objects.get(pk=1), usu_id_rol=Rol.objects.get(pk=1)),
        ])
    

    
    
    
    
    
    
    
