from django.db import models
from doctors.models import Doctor
# from Client.models import Patient
from django.conf import settings
User = settings.AUTH_USER_MODEL
from datetime import timedelta,datetime

# Create your models here.
class Book(models.Model):
    start_time = models.TimeField(unique=True)
    # end_time = models.TimeField(null=True,blank=True)
    date= models.DateField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    busy=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor.fullname} ga qabul"

