# Generated by Django 2.1.5 on 2019-01-31 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20190131_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='fascia_parent',
            field=models.CharField(choices=[('lif', 'Izaje'), ('fas', 'Fascia'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fun', 'Cimentación'), ('spr', 'Spreader'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='fundation_parent',
            field=models.CharField(choices=[('lif', 'Izaje'), ('fas', 'Fascia'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fun', 'Cimentación'), ('spr', 'Spreader'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='lifting_parent',
            field=models.CharField(choices=[('lif', 'Izaje'), ('fas', 'Fascia'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fun', 'Cimentación'), ('spr', 'Spreader'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='paint_parent',
            field=models.CharField(choices=[('lif', 'Izaje'), ('fas', 'Fascia'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fun', 'Cimentación'), ('spr', 'Spreader'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='signage_parent',
            field=models.CharField(choices=[('lif', 'Izaje'), ('fas', 'Fascia'), (' ', 'Sin prescedencia'), ('pan', 'Pintura'), ('fun', 'Cimentación'), ('spr', 'Spreader'), ('sig', 'Rótulos')], default='', max_length=20),
        ),
    ]