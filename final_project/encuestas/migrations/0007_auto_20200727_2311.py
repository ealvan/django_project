# Generated by Django 2.1.5 on 2020-07-27 23:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0006_auto_20200727_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pub_fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 23, 11, 36, 101226, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
