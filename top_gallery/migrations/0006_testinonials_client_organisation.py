# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-21 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0005_auto_20160310_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinonials',
            name='client_organisation',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
