# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('button_title', models.CharField(max_length=100)),
                ('button_link', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
