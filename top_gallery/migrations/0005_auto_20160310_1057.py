# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0004_testinonials_client_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinonials',
            name='text',
            field=models.CharField(max_length=1300, blank=True),
        ),
    ]
