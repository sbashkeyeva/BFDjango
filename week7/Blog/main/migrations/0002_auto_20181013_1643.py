# Generated by Django 2.1.2 on 2018-10-13 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='date_published',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 13, 16, 43, 34, 677407)),
        ),
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 13, 16, 43, 34, 677407)),
        ),
    ]
