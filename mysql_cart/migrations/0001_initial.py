# Generated by Django 3.1.5 on 2021-01-28 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SKUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=30, unique=True)),
                ('mfg', models.CharField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'must be 2 characters or more.')])),
                ('name', models.CharField(default='', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'must be 2 characters or more.')])),
                ('desc', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
