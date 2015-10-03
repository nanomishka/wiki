# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikitest', '0005_files_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='url',
            field=models.CharField(unique=True, max_length=40),
        ),
    ]
