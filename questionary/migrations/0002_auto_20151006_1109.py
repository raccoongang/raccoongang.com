# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='logo',
            field=models.ImageField(upload_to=b'images', blank=True),
        ),
    ]

