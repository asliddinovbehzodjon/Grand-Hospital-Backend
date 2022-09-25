from django.db import models
from django.utils.html import format_html
# Create your models here.
class Drug(models.Model):
    title = models.CharField(max_length=1500,verbose_name="Drug",help_text="Enter drug name")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to="drugs-images")
    expiration_date = models.DateTimeField()
    price = models.CharField(max_length=6000000,default="15000")
    def __str__(self):
        return self.title

    @property
    def image_show(self):
        return format_html('<img src={} width="50" height="50" style="border-radius:50%"'.format(self.image.url))
