# Generated by Django 5.0.2 on 2024-03-11 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('cargo_id', models.AutoField(primary_key=True, serialize=False)),
                ('cargo_nombre', models.CharField(max_length=200)),
                ('cargo_sueldo_basico', models.IntegerField()),
                ('cargo_empresa', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usu_id', models.AutoField(primary_key=True, serialize=False)),
                ('usu_cedula', models.IntegerField(unique=True)),
                ('usu_nombre', models.CharField(max_length=200)),
                ('usu_correo', models.CharField(max_length=200)),
                ('usu_telefono', models.IntegerField()),
                ('usu_contraseña', models.CharField(max_length=200)),
                ('usu_direccion', models.CharField(max_length=200)),
                ('usu_fecha_ingreso', models.DateField()),
                ('usu_estado', models.CharField(max_length=200)),
                ('usu_antiguedad', models.DateField()),
                ('usu_id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.cargo')),
                ('usu_id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.rol')),
            ],
        ),
    ]
