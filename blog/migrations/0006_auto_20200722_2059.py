# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-22 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200722_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(),
        ),
    ]
