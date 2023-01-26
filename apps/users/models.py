from django.db import models
from django.conf import settings


class Vacations(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_time = models.DateTimeField(auto_now_add=True)
    startdate = models.DateField()
    finishdate = models.DateField()
    supervisor = models.CharField(max_length=30, blank=True)
    jun_hr = models.CharField(max_length=30, blank=True)
    head_hr = models.CharField(max_length=30, blank=True)
    director = models.CharField(max_length=30, blank=True)
    comments = models.CharField(max_length=100, blank=True)




