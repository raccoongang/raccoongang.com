# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0002_auto_20151005_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='logo',
            field=models.ImageField(upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='edxproject',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 6, 11, 22, 27, 325412), blank=True),
        ),
    ]
