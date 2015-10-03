# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikitest', '0002_files_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='user',
            field=models.CharField(default=b'anonim', max_length=40),
        ),
    ]
