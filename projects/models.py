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
    # Budget
    budget_allocated = models.IntegerField()
    dollar = models.FloatField()
    # Time
    goal_time = models.IntegerField()
    contractor = models.ForeignKey(Contractor, on_delete=models.DO_NOTHING)
    # Project Manager
    project_manager = models.ForeignKey(
        ProjectManager, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    # Gantt data
    fascia_start = models.DateTimeField(default=datetime.now, blank=True)
    fascia_end = models.DateTimeField(default=datetime.now, blank=True)
    fascia_parent = models.CharField(
        default=' ', max_length=4, choices=choices.ganttimage_choices)
    paint_start = models.DateTimeField(default=datetime.now, blank=True)
    paint_end = models.DateTimeField(default=datetime.now, blank=True)
    paint_parent = models.CharField(
        default=' ', max_length=20, choices=choices.ganttimage_choices)
    signage_start = models.DateTimeField(default=datetime.now, blank=True)
    signage_end = models.DateTimeField(default=datetime.now, blank=True)
    signage_parent = models.CharField(
        default=' ', max_length=20, choices=choices.ganttimage_choices)
    fundation_start = models.DateTimeField(default=datetime.now, blank=True)
    fundation_end = models.DateTimeField(default=datetime.now, blank=True)
    fundation_parent = models.CharField(
        default=' ', max_length=20, choices=choices.ganttimage_choices)
    lifting_star = models.DateTimeField(default=datetime.now, blank=True)
    lifting_end = models.DateTimeField(default=datetime.now, blank=True)
    lifting_parent = models.CharField(
        default=' ', max_length=20, choices=choices.ganttimage_choices)

    def __str__(self):
        return self.name


class GanttImage(models.Model):
    # Completion
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    fascia_completion = models.DecimalField(max_digits=3, decimal_places=2)
    spreader_completion = models.DecimalField(max_digits=3, decimal_places=2)
    paint_completion = models.DecimalField(max_digits=3, decimal_places=2)
    signage_completion = models.DecimalField(max_digits=3, decimal_places=2)
    fundation_completion = models.DecimalField(max_digits=3, decimal_places=2)
    lifting_completion = models.DecimalField(max_digits=3, decimal_places=2)
    report_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.report_date
