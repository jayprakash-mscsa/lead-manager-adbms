from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, LeadAssigneeViewSet, PartnerViewSet, PartnerEmployeeViewSet, ServiceViewSet, InteractionViewSet

# Create a router and register all the ViewSets
router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'lead-assignees', LeadAssigneeViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'partner-employees', PartnerEmployeeViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'interactions', InteractionViewSet)

# Include the router in the URLs
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]