from email.mime import message
from django.db import models

class Contacts(models.Model):
    first_name=models.CharField(max_length = 25, blank=True, null=True)
    last_name = models.CharField(max_length = 75, blank=True, null=True)
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    phone= models.CharField(max_length = 20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    city = models.CharField(max_length = 100, blank=True, null=True)
    country = models.CharField(max_length = 100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length = 5, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True, null=True)   
    def __str__(self):
        return self.name
