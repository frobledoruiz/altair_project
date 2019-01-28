from datetime import datetime

from django.db import models


SCOPE_CHOICES = (
    ('fuel', 'Combustibles'),
    ('imag', 'Imagen'),
    ('cons', 'Consultoría'),
    ('lice', 'Permisos y Licencias'),
    ('desi', 'Diseños')
)


class Contractor(models.Model):
    name = models.CharField(max_length=200)
    contractor_logo = models.ImageField(upload_to='photos/contractors/%Y/%m')
    scope = models.CharField(max_length=40, choices=SCOPE_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
