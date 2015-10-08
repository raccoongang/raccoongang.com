# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0002_auto_20151006_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edxproject',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 6, 11, 9, 20, 224164), blank=True),
        ),
    ]

