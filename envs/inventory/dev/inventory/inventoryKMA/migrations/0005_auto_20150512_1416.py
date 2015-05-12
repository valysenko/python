# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0004_auto_20150511_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='message',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(0)], max_length=600),
        ),
    ]
