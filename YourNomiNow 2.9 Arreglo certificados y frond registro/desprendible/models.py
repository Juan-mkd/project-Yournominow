from django.db import models
from usuario.models import Usuario
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
    deveng_fecha = models.DateField()
    




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
    
    
class Nomina(models.Model):
    nom_id = models.AutoField(primary_key=True)
    nom_cedula = models.ForeignKey(Usuario, to_field='cedula', on_delete=models.CASCADE)
    nom_fecha_creacion = models.DateField()
    nom_tipo_pago = models.CharField(max_length=200)
    nom_periodo_pago = models.DateField()
    nom_dias_trabajados = models.IntegerField()