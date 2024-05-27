# Generated by Django 5.0.4 on 2024-05-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desprendible', '0005_descuento_des_time_retardo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores_fijos',
            fields=[
                ('valor_id', models.AutoField(primary_key=True, serialize=False)),
                ('valor_trasporte', models.IntegerField()),
                ('valor_alimentacion', models.IntegerField()),
                ('valor_aport_salud', models.IntegerField()),
                ('valor_aport_pension', models.IntegerField()),
                ('valor_aport_sena', models.IntegerField()),
                ('valor_aport_icbf', models.IntegerField()),
            ],
        ),
    ]
