# Generated by Django 2.1.3 on 2018-11-05 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181105_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 5, 10, 20, 50, 740672, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='dueon',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 7, 10, 20, 50, 740704, tzinfo=utc)),
        ),
    ]
