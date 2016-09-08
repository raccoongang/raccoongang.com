# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0007_auto_20160303_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinonials',
            name='client_organisation',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
