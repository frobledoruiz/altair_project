# Generated by Django 2.1.5 on 2019-01-30 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190130_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget_allocated',
            field=models.IntegerField(),
        ),
    ]
