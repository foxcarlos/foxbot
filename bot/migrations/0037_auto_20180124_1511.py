# Generated by Django 2.0.1 on 2018-01-24 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0036_auto_20180124_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertausuario',
            name='ultima_actualizacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 24, 15, 11, 34, 39824), null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 24, 15, 11, 34, 41142)),
        ),
    ]