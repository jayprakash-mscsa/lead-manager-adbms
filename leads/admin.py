from django.contrib import admin
from .models import Lead, Service, Partner, PartnerEmployee, LeadAssignee, Interaction,InteractionType, CallStatus, CallInteraction

class CallInteractionInline(admin.TabularInline):
    model = CallInteraction
    extra = 1  # Number of empty forms to display

class InteractionAdmin(admin.ModelAdmin):
    inlines = [CallInteractionInline]
    list_display = ('interaction_type', 'lead', 'employee', 'timestamp')
    search_fields = ('lead__email', 'employee__name') 

admin.site.register(Lead)
admin.site.register(Service)
admin.site.register(Partner)
admin.site.register(PartnerEmployee)
admin.site.register(LeadAssignee)
admin.site.register(Interaction, InteractionAdmin)
admin.site.register(InteractionType)
admin.site.register(CallStatus)