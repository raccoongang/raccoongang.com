# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edxproject',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 18, 20, 17, 395248), blank=True),
        ),
    ]
