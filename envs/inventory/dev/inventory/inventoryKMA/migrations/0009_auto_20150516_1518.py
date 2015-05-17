# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0008_auto_20150516_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='message',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(0)], max_length=500),
        ),
    ]
