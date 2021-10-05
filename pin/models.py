from os import posix_fallocate
from django.db import models

class Pincode(models.Model):
    pin         = models.CharField(max_length=15)
    region      = models.CharField(max_length=70)
    place       = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=60)

    def __str__(self):
        return self.pin