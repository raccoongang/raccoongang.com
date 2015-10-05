# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdxProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=48)),
                ('expire_date', models.DateField(default=datetime.datetime(2015, 10, 1, 14, 0, 32, 335720), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to=b'uploads/')),
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
                ('edx_project', models.ForeignKey(to='questionary.EdxProject')),
            ],
        ),
        migrations.AddField(
            model_name='formgallery',
            name='formstep',
            field=models.ForeignKey(to='questionary.FormStep'),
        ),
    ]
