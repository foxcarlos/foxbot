# Generated by Django 2.0.1 on 2018-01-25 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0044_auto_20180124_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertausuario',
            name='ultima_actualizacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 25, 15, 55, 57, 424732), null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 25, 15, 55, 57, 425931)),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='descripcion',
            field=models.CharField(blank=True, default='Sin Descripcion', max_length=200, null=True),
        ),
    ]
