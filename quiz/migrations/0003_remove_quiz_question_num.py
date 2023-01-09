# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170715_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='question_num',
        ),
    ]
