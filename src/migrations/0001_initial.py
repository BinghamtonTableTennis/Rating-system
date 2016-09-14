# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
            options={
                'db_table': 'visits',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=10)),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner_fname', models.CharField(max_length=10)),
                ('winner_lname', models.CharField(max_length=10)),
                ('loser_fname', models.CharField(max_length=10)),
                ('loser_lname', models.CharField(max_length=10)),
                ('winner_score', models.IntegerField()),
                ('loser_score', models.IntegerField()),
                ('day', models.DateField()),
            ],
            options={
                'db_table': 'matches',
            },
        ),
    ]
