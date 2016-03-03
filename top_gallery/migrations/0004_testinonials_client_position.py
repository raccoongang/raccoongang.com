# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0003_auto_20160218_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinonials',
            name='client_position',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
