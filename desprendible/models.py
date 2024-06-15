from django.db import models
from usuario.models import Usuario
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.utils import timezone
# Create your models here.

class Devengado(models.Model):
    deveng_id= models.AutoField(primary_key=True)
    deveng_cedula = models.ForeignKey(Usuario, to_field='cedula', on_delete=models.CASCADE, unique=False)
    deveng_subs_trans = models.IntegerField()
    deveng_subs_alim = models.IntegerField()
    deveng_horas_extra_diur = models.IntegerField()
    deveng_horas_extra_noct = models.IntegerField()
    deveng_horas_extra_diur_domfest = models.IntegerField()
    deveng_horas_extra_noct_domfest = models.IntegerField()
    deveng_bonificacion = models.IntegerField()
    deveng_periodo_pago = models.DateField()
    deveng_tipo_descuento = models.TextField(max_length=50, default='fiscal')
    deveng_fecha = models.DateField()
    total_devengados =models.IntegerField(null=True)




class Descuento(models.Model):
    desc_id = models.AutoField(primary_key=True)
    desc_cedula = models.ForeignKey(Usuario, to_field='cedula', on_delete=models.CASCADE,unique=False)
    desc_creditos_libranza = models.IntegerField()
    desc_cuotas_sindicales = models.IntegerField()
    desc_embargos_judiciales = models.IntegerField()
    desc_periodo_pago = models.DateField()
    desc_tipo_descuento = models.TextField()
    desc_precio = models.IntegerField()
    desc_fecha_des = models.DateField()
    des_time_retardo = models.IntegerField()
    total_descuentos = models.IntegerField(null=True)
    
    def __str__(self):
        return f"Descuento #{self.desc_id} - Cédula Usuario: {self.desc_cedula.cedula}"
    
    
class Nomina(models.Model):
    nom_id = models.AutoField(primary_key=True)
    nom_cedula = models.ForeignKey(Usuario, to_field='cedula', on_delete=models.CASCADE)
    nom_fecha_creacion = models.DateField()
    nom_tipo_pago = models.CharField(max_length=200)
    nom_periodo_pago = models.DateField()
    nom_dias_trabajados = models.IntegerField()
    total_neto = models.IntegerField(null=True)
    estado = models.CharField(max_length=50, default='pendiente')
    
    
class Valores_fijos(models.Model):
    valor_id = models.AutoField(primary_key=True)
    valor_trasporte = models.IntegerField()
    valor_alimentacion = models.IntegerField()
    valor_aport_salud = models.FloatField()
    valor_aport_pension = models.FloatField()
    valor_aport_sena = models.FloatField()
    valor_aport_icbf = models.FloatField()
    
@receiver(post_migrate)
def insertValores(sender, **kwargs):
    if kwargs.get('app_config'):
        app_name= kwargs['app_config'].name
        if app_name == 'desprendible':
            Valores_fijos.objects.bulk_create([
                Valores_fijos(valor_id="1", valor_trasporte="160000 ", valor_alimentacion="0", valor_aport_salud="0.04", valor_aport_pension="0.04", valor_aport_sena="0.04", valor_aport_icbf="0.04",),
        ])

@receiver(post_migrate)
def insertDevengados(sender, **kwargs):
    if kwargs.get('app_config'):
        app_name= kwargs['app_config'].name
        if app_name == 'desprendible':
            Devengado.objects.bulk_create([
                Devengado(deveng_subs_trans= 0, 
                          deveng_subs_alim= 0, 
                          deveng_horas_extra_diur= 0, 
                          deveng_horas_extra_noct= 0, 
                          deveng_horas_extra_diur_domfest= 0, 
                          deveng_horas_extra_noct_domfest= 0, 
                          deveng_bonificacion= 0,
                          deveng_periodo_pago= timezone.now(),
                          deveng_fecha= timezone.now(),
                          deveng_cedula_id='123',
                          total_devengados=0,),
                        ])
            
@receiver(post_migrate)
def insertDescuentos(sender, **kwargs):
    if kwargs.get('app_config'):
        app_name= kwargs['app_config'].name
        if app_name == 'desprendible':
            Descuento.objects.bulk_create([
                Descuento(desc_cedula_id='123',
                          desc_periodo_pago=timezone.now(),
                          desc_creditos_libranza=0,
                          desc_cuotas_sindicales=0,
                          desc_embargos_judiciales=0,
                          desc_precio=0,
                          desc_tipo_descuento="fiscal",
                          desc_fecha_des=timezone.now(),
                          des_time_retardo=0,),
                        ])
            
@receiver(post_migrate)
def insertNominas(sender, **kwargs):
    if kwargs.get('app_config'):
        app_name= kwargs['app_config'].name
        if app_name == 'desprendible':
            Nomina.objects.bulk_create([
                Nomina(nom_cedula_id='123',
                        nom_fecha_creacion=timezone.now(),
                        nom_tipo_pago="Electronico",
                        nom_periodo_pago=timezone.now(),
                        nom_dias_trabajados=0,
                        total_neto=0,
                        estado='inicial',),
                        ])