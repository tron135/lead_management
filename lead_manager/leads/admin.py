from django.contrib import admin

from .models import Lead, FollowUp
# Register your models here.

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'phone_number', 'creation_time', 'contact_person', 'current_stage')
    fieldsets = [(None, {'fields': ('creation_time', 'source', 'contact_person', 'name', 'current_stage')})]

class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('lead_name', 'medium_used', 'date_followed')


admin.site.register(FollowUp, FollowUpAdmin)
admin.site.register(Lead, LeadAdmin)