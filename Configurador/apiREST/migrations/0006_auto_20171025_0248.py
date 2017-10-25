# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiREST', '0005_auto_20171025_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='photo_url',
            new_name='photo_normal',
        ),
        migrations.AddField(
            model_name='character',
            name='photo_super',
            field=models.CharField(default='/', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='photo_ultra',
            field=models.CharField(default='/', max_length=200),
            preserve_default=False,
        ),
    ]
