# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikitest', '0004_remove_files_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='url',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
