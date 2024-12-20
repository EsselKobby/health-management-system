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