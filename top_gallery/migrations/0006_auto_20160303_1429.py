# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinonials',
            name='text',
            field=models.CharField(max_length=600, blank=True),
        ),
    ]
