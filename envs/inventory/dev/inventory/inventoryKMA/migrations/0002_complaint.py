# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryKMA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(0)])),
                ('unit_item', models.ForeignKey(null=True, related_name='complaints', to='inventoryKMA.UnitItem')),
            ],
        ),
    ]
