from django.db import models
from django.contrib.auth.models import User

# Create your models here
# Band Profile Model

class BandProfile(models.Model):
    bandName = models.CharField(max_length=50)
    bandSummary = models.CharField(max_length=600)
    bandImage =  models.ImageField(upload_to='images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bandName
        return self.bandSummary

