# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0003_auto_20150511_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='number',
            field=models.CharField(default=1, max_length=3, validators=[django.core.validators.MinLengthValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workplace',
            name='number',
            field=models.CharField(default=2, max_length=3, validators=[django.core.validators.MinLengthValidator(0)]),
            preserve_default=False,
        ),
    ]
