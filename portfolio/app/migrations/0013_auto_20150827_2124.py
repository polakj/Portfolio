# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20150827_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb_url',
            field=models.ImageField(upload_to='/home/jacek/nauka/Portfolio/portfolioapp/files/img/projects'),
        ),
    ]
