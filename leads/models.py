from django.db import models
from django.contrib.auth.models import User

# Partners (companies using your app)
class Partner(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

# Services (what services a partner provides)
class Service(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# PartnerEmployees (employees working for a partner)
class PartnerEmployee(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='employees')
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Assuming you are using Django's built-in User model
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.partner.name}"

# Leads (customer inquiries for a partner)
class Lead(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='leads')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='leads')
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead from {self.customer_name} for {self.partner.name}"
    
class InteractionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)  # Optional field for more details

    def __str__(self):
        return self.name

class CallStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Call Status"
        verbose_name_plural = "Call Statuses"

    def __str__(self):
        return self.name
    
class Interaction(models.Model):
    lead = models.ForeignKey(Lead, related_name='interactions', on_delete=models.CASCADE)
    employee = models.ForeignKey(PartnerEmployee, related_name='interactions', on_delete=models.CASCADE)
    interaction_type = models.ForeignKey(InteractionType, related_name='interactions', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.interaction_type.name} with {self.lead.customer_email} by {self.employee} on {self.timestamp}"

class CallInteraction(models.Model):
    interaction = models.ForeignKey(Interaction, related_name='call_interactions', on_delete=models.CASCADE)
    call_status = models.ForeignKey(CallStatus, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)  # Optional field for additional notes

    def __str__(self):
        return f"Call Interaction: {self.interaction.id} - Status: {self.call_status.name}"
    
# LeadAssignees (leads assigned to partner employees)
class LeadAssignee(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='assignees')
    employee = models.ForeignKey(PartnerEmployee, on_delete=models.CASCADE, related_name='assigned_leads')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead {self.lead.id} assigned to {self.employee.user.username}"

