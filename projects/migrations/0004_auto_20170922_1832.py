# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-22 16:32
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160928_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, keep_meta=True, null=True, quality=0, size=[500, 500], upload_to='project_pictures'),
        ),
    ]