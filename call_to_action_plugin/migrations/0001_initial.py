# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToActionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cms.CMSPlugin', primary_key=True, auto_created=True)),
                ('block_to_show', models.ForeignKey(to='core.Block')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
