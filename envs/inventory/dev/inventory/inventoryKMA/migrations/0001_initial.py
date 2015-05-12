# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('columns', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('rows', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('assistant', models.OneToOneField(related_name='classroom_assistant', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(validators=[django.core.validators.MinLengthValidator(0)], max_length=15)),
                ('status', models.CharField(validators=[django.core.validators.MinLengthValidator(0)], max_length=15)),
                ('assistant', models.ForeignKey(related_name='tasks', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UnitItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(validators=[django.core.validators.MinLengthValidator(0)], max_length=15)),
                ('unit', models.OneToOneField(to='inventoryKMA.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom', models.ForeignKey(to='inventoryKMA.Classroom')),
            ],
        ),
        migrations.AddField(
            model_name='unititem',
            name='workplace',
            field=models.ForeignKey(to='inventoryKMA.Workplace'),
        ),
    ]
