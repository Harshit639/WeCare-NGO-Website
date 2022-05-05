from django.db import models
from django.urls import reverse
# Create your models here.
class donateUs(models.Model):
    name=models.CharField(blank=False,max_length=256)
    email=models.EmailField(blank=False,default='')
    money=models.IntegerField('Amount in Rs.')
    phone=models.IntegerField('Phone No.')

    def __str__(self):
        return self.amount

    def get_absolute_url(self):
        return reverse('test')
