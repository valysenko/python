# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0002_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='assistant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='classroom_assistant'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='unit_item',
            field=models.ForeignKey(to='inventoryKMA.Workplace', null=True, related_name='complaints'),
        ),
    ]
