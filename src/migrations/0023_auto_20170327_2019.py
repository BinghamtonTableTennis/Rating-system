# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-28 00:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0022_auto_20170327_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Address1',
            new_name='Address1',
        ),
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Address2',
            new_name='Address2',
        ),
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Bengaged',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Email',
            new_name='Facebook',
        ),
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Facebook',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Name',
            new_name='Other_Website',
        ),
        migrations.RenameField(
            model_name='organizationinformation',
            old_name='Organization_Youtube',
            new_name='Youtube',
        ),
    ]