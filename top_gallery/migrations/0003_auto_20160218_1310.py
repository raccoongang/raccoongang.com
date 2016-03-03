# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_gallery', '0002_auto_20150911_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testinonials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200, blank=True)),
                ('client_name', models.CharField(max_length=150, blank=True)),
                ('link', models.CharField(max_length=128, blank=True)),
                ('file', models.ImageField(upload_to=b'images')),
            ],
        ),
        migrations.CreateModel(
            name='TestinonialsGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='testinonials',
            name='gallery',
            field=models.ForeignKey(to='top_gallery.TestinonialsGallery'),
        ),
    ]
