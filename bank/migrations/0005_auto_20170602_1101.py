# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20170531_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_logo',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='a',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
