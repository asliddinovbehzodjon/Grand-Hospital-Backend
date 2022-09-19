from django.db import models
from django.utils.html import format_html
# Create your models here.
class Doctor(models.Model):
    fullname = models.CharField(max_length=600,help_text="Enter doctor fullname",verbose_name="Doctor name")
    image = models.ImageField(upload_to='doctor-image',verbose_name="Doctor image",help_text="Upload doctor image")
    profession = models.CharField(max_length=600,help_text="Enter doctor profession",verbose_name="Doctor profession")
    phone = models.CharField(max_length=600,verbose_name="Doctor phone number",help_text="Enter phone number")
    address = models.CharField(max_length=600,help_text="Enter doctor address",verbose_name="Doctor adress")
    job = models.CharField(max_length=800,help_text="Enter doctor position",verbose_name="Doctor position")
    @property
    def image_show(self):
        return format_html('<img src={} width="50" height="50" style="border-radius:50%"'.format(self.image.url))
        
    def __str__(self):
        return self.fullname
