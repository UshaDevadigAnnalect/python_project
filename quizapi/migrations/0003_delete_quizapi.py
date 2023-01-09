# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapi', '0002_auto_20170727_0922'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuizApi',
        ),
    ]
