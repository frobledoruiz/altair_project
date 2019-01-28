from datetime import datetime

from django.db import models


ZONES_CHOICES = (
    ('nor', 'Norte'),
    ('cen', 'Centro'),
    ('sur', 'Sur'),
    ('all', 'Todas'),
)


class ProjectManager(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='photos/pms/%Y/%m')
    zone = models.CharField(max_length=20, choices=ZONES_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
