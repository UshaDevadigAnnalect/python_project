# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock',
            new_name='QuizApi',
        ),
    ]
