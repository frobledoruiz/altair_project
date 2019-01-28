from datetime import datetime
from email.policy import default

from django.db import models

from contractors.models import Contractor
from pms.models import ProjectManager
from projects import choices


class Project(models.Model):
    name = models.CharField(max_length=200)
    main_photo = models.ImageField(upload_to='photos/projects/%Y/%m')
    city = models.CharField(
        max_length=30, choices=choices.CIUDADES_CHOICES, default='BOG')
    state = models.CharField(
        max_length=30, choices=choices.DEPARTAMENTOS_CHOICES, default='CUN')
    scope = models.CharField(max_length=50, choices=choices.SCOPE_CHOICES)
    zone = models.CharField(max_length=4, choices=choices.ZONES_CHOICES)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    is_active = models.BooleanField(default=False)
    budget_allocated = models.FloatField()
    dollar = models.FloatField()
    goal_time = models.FloatField()
    contractor = models.ForeignKey(Contractor, on_delete=models.DO_NOTHING)
    project_manager = models.ForeignKey(
        ProjectManager, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name