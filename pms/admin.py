from django.contrib import admin

from .models import ProjectManager


class ProjectManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zone', 'phone',
                    'email', 'is_active', 'hire_date')
    list_display_links = ('id', 'name', 'zone')
    list_filter = ('name',)
    search_fields = ('name', 'zone')
    list_editable = ('is_active',)
    list_per_page = 15


admin.site.register(ProjectManager, ProjectManagerAdmin)
