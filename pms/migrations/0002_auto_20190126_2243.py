# Generated by Django 2.1.5 on 2019-01-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmanager',
            name='zone',
            field=models.CharField(choices=[('nor', 'Norte'), ('cen', 'Centro'), ('sur', 'Sur'), ('all', 'Todas')], max_length=20),
        ),
    ]
