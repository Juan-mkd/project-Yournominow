# Generated by Django 5.0.4 on 2024-05-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desprendible', '0008_devengado_total_devengados'),
    ]

    operations = [
        migrations.AddField(
            model_name='descuento',
            name='total_descuentos',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nomina',
            name='total_neto',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
