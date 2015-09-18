# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='button_link',
            field=models.CharField(blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='button_title',
            field=models.CharField(blank=True, max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True),
            preserve_default=True,
        ),
    ]
