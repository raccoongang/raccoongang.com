# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import questionary.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eav', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to=b'')),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='FormStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('attribute', questionary.fields.OneToManyField(to='eav.Attribute')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='formgallery',
            name='formstep',
            field=models.ForeignKey(to='questionary.FormStep'),
        ),
    ]
