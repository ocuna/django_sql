# Generated by Django 3.1.5 on 2021-02-02 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysql_hr', '0008_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysql_hr.employee')),
            ],
        ),
    ]
