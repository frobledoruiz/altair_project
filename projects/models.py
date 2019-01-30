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
        max_length=30, choices=choices.city_choices, default='BOG')
    state = models.CharField(
        max_length=30, choices=choices.state_choices, default='CUN')
    scope = models.CharField(max_length=50, choices=choices.scope_choices)
    zone = models.CharField(max_length=4, choices=choices.zone_choices)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    is_active = models.BooleanField(default=False)
    budget_allocated = models.IntegerField()
    dollar = models.FloatField()
    goal_time = models.IntegerField()
    contractor = models.ForeignKey(Contractor, on_delete=models.DO_NOTHING)
    project_manager = models.ForeignKey(
        ProjectManager, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
