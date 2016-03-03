# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_to_action_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calltoactionplugin',
            name='google_event',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
