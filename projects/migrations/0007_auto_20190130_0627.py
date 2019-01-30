# Generated by Django 2.1.5 on 2019-01-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190130_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='city',
            field=models.CharField(choices=[('BAR', 'Barranquilla'), ('MED', 'Medellín'), ('CAR', 'Cartagena'), ('BOG', 'Bogota DC'), ('STA', 'Santa Marta'), ('CAL', 'Cali'), ('PAS', 'Pasto'), ('VIL', 'Villavicencio'), ('IBG', 'Ibagué')], default='BOG', max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('AMA', 'Amazonas'), ('ANT', 'Antioquia'), ('ARA', 'Arauca'), ('ARC', 'Archipielago de San Andrés, Prov. y Sta Catalina'), ('ATL', 'Atlántico'), ('BOL', 'Bolivar'), ('BOY', 'Boyacá'), ('CAL', 'Caldas'), ('CAQ', 'Caquetá'), ('CAS', 'Casanare'), ('CAU', 'Cauca'), ('CES', 'Cesar'), ('CHO', 'Chocó'), ('COR', 'Córdoba'), ('CUN', 'Cundinamarca'), ('GUA', 'Guainía'), ('GUV', 'Guaviare'), ('HUI', 'Huila'), ('LAG', 'La Guajira'), ('MAG', 'Magdalena'), ('MET', 'Meta'), ('NAR', 'Nariño'), ('NOR', 'Norte de Santander'), ('PUT', 'Putumayo'), ('QUI', 'Quindío'), ('RIS', 'Risaralda'), ('SAN', 'Santander'), ('SUC', 'Sucre'), ('TOL', 'Tolima'), ('VCA', 'Valle del Cauca'), ('VAU', 'Vaupés'), ('VIC', 'Vichada')], default='CUN', max_length=30),
        ),
    ]