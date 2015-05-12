# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0006_unititem_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unititem',
            name='field',
        ),
        migrations.AlterField(
            model_name='unititem',
            name='unit',
            field=models.ForeignKey(to='inventoryKMA.Unit'),
        ),
    ]
