# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopGalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cms.CMSPlugin', primary_key=True, auto_created=True)),
                ('gallery', models.ForeignKey(to='top_gallery.Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
