# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(max_length=200, upload_to=''),
        ),
    ]
