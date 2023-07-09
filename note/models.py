from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
