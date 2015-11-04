# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0003_auto_20151007_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='formgallery',
            name='data_attribute',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='edxproject',
            name='expire_date',
            field=models.DateField(default=datetime.datetime.now, blank=True),
        ),
    ]
