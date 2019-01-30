from django.contrib import admin

from .models import Project, GanttImage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scope', 'zone', 'city', 'state', 'budget_allocated', 'dollar',
                    'goal_time', 'contractor', 'project_manager', 'create_date', 'is_active', 'is_published')
    list_display_links = ('id', 'name', 'scope', 'zone', 'contractor')
    list_filter = ('name', 'scope', 'zone', 'project_manager')
    search_fields = ('name', 'scope', 'zone', 'city',
                     'state', 'project_manger')
    list_editable = ('is_active', 'is_published')
    list_per_page = 25


class GanttImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'report_date')
    list_display_links = ('id', 'project')
    list_per_page = 25


admin.site.register(Project, ProjectAdmin)
admin.site.register(GanttImage, GanttImageAdmin)
