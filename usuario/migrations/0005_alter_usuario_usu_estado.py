# Generated by Django 5.0.3 on 2024-03-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0004_alter_usuario_usu_id_rol"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="usu_estado",
            field=models.CharField(default="activo", max_length=200),
        ),
    ]
