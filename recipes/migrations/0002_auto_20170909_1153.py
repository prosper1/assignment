# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-09 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipepost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recipepost',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='cooking_time',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='prep_time',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='recipepost',
            name='servings',
            field=models.CharField(max_length=15),
        ),
    ]