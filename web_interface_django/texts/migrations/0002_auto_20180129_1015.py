# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='source_url',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
