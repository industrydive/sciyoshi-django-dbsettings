# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-27 13:21
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import migrations

from dbsettings.settings import USE_SITES

def define_unique_set():
    if USE_SITES:
        return set([('site', 'module_name', 'class_name', 'attribute_name')])
    else:
        return set([('module_name', 'class_name', 'attribute_name')])


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('dbsettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='setting',
            unique_together=define_unique_set(),
        ),
    ]
