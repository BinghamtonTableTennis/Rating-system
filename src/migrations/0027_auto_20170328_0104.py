# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-28 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0026_auto_20170328_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationinformation',
            name='Year_First_Established',
        ),
        migrations.AddField(
            model_name='organizationinformation',
            name='Copyright_Year',
            field=models.CharField(default='2017', max_length=20),
            preserve_default=False,
        ),
    ]