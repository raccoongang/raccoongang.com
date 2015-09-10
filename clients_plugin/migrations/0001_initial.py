# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('top_gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, to='cms.CMSPlugin', parent_link=True)),
                ('clients', models.ForeignKey(to='top_gallery.Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
