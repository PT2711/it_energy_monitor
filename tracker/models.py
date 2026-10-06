from django.db import models

class ITLabEnergy(models.Model):
    LAB_CHOICES = [
        ('Server Room', 'Central Server Room'),
        ('AI & DS Lab', 'AI & Data Science Lab'),
        ('Network Lab', 'Networking & Security Lab'),
        ('Software Lab', 'Software Engineering Lab'),
        ('Cloud Lab', 'Cloud Computing Lab'),
    ]

    lab_name = models.CharField(max_length=50, choices=LAB_CHOICES)
    device_type = models.CharField(max_length=100)
    units_kwh = models.FloatField()
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lab_name} - {self.device_type} ({self.units_kwh} kWh)"