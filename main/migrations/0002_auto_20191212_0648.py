# Generated by Django 2.2.7 on 2019-12-12 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asutus',
            name='avamise_kellaaeg',
            field=models.TimeField(default=datetime.time(8, 30)),
        ),
        migrations.AddField(
            model_name='asutus',
            name='sulgemise_kellaaeg',
            field=models.TimeField(default=datetime.time(19, 30)),
        ),
    ]
