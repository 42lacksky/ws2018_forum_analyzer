# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0002_auto_20180131_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='summary',
            field=models.TextField(max_length=10000),
        ),
    ]
