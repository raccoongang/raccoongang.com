# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusemail',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
