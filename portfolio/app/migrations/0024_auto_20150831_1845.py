# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20150831_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(upload_to='projects/', height_field='185'),
        ),
    ]
