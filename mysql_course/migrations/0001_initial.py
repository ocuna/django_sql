# Generated by Django 3.1.5 on 2021-01-26 03:08

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'Must be 5 characters or more.')])),
                ('description', models.TextField(default='', validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('instructor', models.CharField(default='', max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'Must be 5 characters or more.')])),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]