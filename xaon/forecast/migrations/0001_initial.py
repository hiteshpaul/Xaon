# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import forecast.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docFile', models.FileField(upload_to=b'', validators=[forecast.validators.validate_file_type], verbose_name='File')),
            ],
        ),
    ]
