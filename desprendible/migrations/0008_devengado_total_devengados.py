# Generated by Django 5.0.4 on 2024-05-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desprendible', '0007_alter_valores_fijos_valor_aport_icbf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devengado',
            name='total_devengados',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
