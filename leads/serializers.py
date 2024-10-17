from rest_framework import serializers
from .models import Lead, LeadAssignee, Partner, PartnerEmployee, Service, Interaction

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"

class LeadAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadAssignee
        fields = "__all__"

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

class PartnerEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerEmployee
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = "__all__"