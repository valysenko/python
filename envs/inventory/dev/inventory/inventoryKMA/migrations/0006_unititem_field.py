# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0005_auto_20150512_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='unititem',
            name='field',
            field=models.CharField(default=2, validators=[django.core.validators.MinLengthValidator(0)], max_length=15),
            preserve_default=False,
        ),
    ]
