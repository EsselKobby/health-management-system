from django.db import models

from shortuuid.django.fields import ShortUUIDField

from doctor import models as doctor_models
from patient import models as patient_models

# Create your models here.
class Service(model.Models):
    image = models.FileField(upload_to="images", null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    available_doctors = models.ManyToManyField(doctors_models.Doctor, blank=True)

    def __str__(self):
        return f"{self.name} - {self.cost}" 

class Appointment(models.Model):
    STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),

    ]

    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='service_appointed')
    doctor = models.ForeignKey(doctor_models.Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_appointments')
    patient = models.ForeignKey(patient_models.Patient, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments_patient')
    appointment_date = models.DateTimeField(null=True, blank=True)
    issues = models.TextField(blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    appointment_id = ShortUUIDField(length=6, max_length=10, alphabet="1234567890")
    status = models.CharField(max_length=120, choices=STATUS)

    def __str__(self):
        return f"{self.patient.full_name} with {self.doctor.full_name}"