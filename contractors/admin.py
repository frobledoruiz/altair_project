from django.contrib import admin

from .models import Contractor

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scope', 'phone', 'email', 'is_active')
    list_display_links = ('id', 'name', 'scope')
    list_filter = ('name',)
    search_fields = ('name', 'scope')
    list_editable = ('is_active',)
    list_per_page = 15

admin.site.register(Contractor, ContractorAdmin)

