# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-01 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputbox', '0002_article_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='writer',
        ),
    ]
