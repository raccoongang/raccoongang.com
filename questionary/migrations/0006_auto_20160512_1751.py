# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0005_survey_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
