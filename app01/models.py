from django.db import models

# Create your models here.

class UseriInfo(models.Model):
    name = models.CharField(max_length=32)