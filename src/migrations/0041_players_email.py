# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-04 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0040_auto_20170404_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='Email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
