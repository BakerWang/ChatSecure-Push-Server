# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
    ]
