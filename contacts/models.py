from django.db import models

class Contacts(models.Model):
    first_name=models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 75)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length = 5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.first_name
    


