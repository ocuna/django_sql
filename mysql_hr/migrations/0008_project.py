# Generated by Django 3.1.5 on 2021-02-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql_hr', '0007_auto_20210125_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=50)),
                ('programmers', models.ManyToManyField(to='mysql_hr.Employee')),
            ],
        ),
    ]
