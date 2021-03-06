# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2020-01-03 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_q', '0011_auto_20190328_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklogger',
            options={'ordering': ('-create_datetime',), 'verbose_name': 'Logging', 'verbose_name_plural': 'Logging'},
        ),
        migrations.RenameField(
            model_name='tasklogger',
            old_name='date',
            new_name='create_datetime',
        ),
        migrations.RenameField(
            model_name='tasklogger',
            old_name='log',
            new_name='msg',
        ),
        migrations.AddField(
            model_name='tasklogger',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NotSet'), (20, 'Info'), (30, 'Warning'), (10, 'Debug'), (40, 'Error'), (50, 'Fatal')], db_index=True, default=40),
        ),
        migrations.AddField(
            model_name='tasklogger',
            name='logger_name',
            field=models.CharField(default='before', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasklogger',
            name='trace',
            field=models.TextField(blank=True, null=True),
        ),
    ]
