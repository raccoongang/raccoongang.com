# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_block_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='subtitle',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
