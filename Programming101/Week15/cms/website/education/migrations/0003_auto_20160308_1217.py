# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20160308_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='endDate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='startDate',
            new_name='start_date',
        ),
    ]
