# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='student',
        ),
        migrations.RemoveField(
            model_name='education',
            name='tenure_end',
        ),
        migrations.RemoveField(
            model_name='education',
            name='tenure_start',
        ),
        migrations.RemoveField(
            model_name='workex',
            name='tenure_end',
        ),
        migrations.RemoveField(
            model_name='workex',
            name='tenure_start',
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Achievement',
        ),
    ]
