# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0007_auto_20150512_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='unit_item',
            new_name='workplace',
        ),
    ]
