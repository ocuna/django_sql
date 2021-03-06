# Generated by Django 3.1.5 on 2021-01-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql_hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passangers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('points', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(),
        ),
    ]
