from django.db import models
from django.urls import reverse
# Create your models here.
class feedback(models.Model):
    email=models.EmailField(blank=False,default='')
    message=models.TextField('Feedback/Queries')

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')
