# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='subtitle',
            field=models.CharField(default='Some subtitle going to be there', max_length=300),
            preserve_default=False,
        ),
    ]
