# Generated by Django 3.1.5 on 2021-01-26 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(default='', max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'must be 2 characters or more.')])),
                ('last', models.CharField(default='', max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'must be 2 characters or more.')])),
                ('email', models.CharField(default='', max_length=254)),
                ('grade', models.FloatField(default=0)),
            ],
        ),
    ]
