# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# views.py

from rest_framework import viewsets
from .models import Lead, LeadAssignee, Partner, PartnerEmployee, Service, Interaction
from .serializers import LeadSerializer, LeadAssigneeSerializer, PartnerSerializer, PartnerEmployeeSerializer, ServiceSerializer, InteractionSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadAssigneeViewSet(viewsets.ModelViewSet):
    queryset = LeadAssignee.objects.all()
    serializer_class = LeadAssigneeSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnerEmployeeViewSet(viewsets.ModelViewSet):
    queryset = PartnerEmployee.objects.all()
    serializer_class = PartnerEmployeeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
