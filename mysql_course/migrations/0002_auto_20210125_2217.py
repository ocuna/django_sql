# Generated by Django 3.1.5 on 2021-01-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql_course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
