from django.contrib.auth.models import User
from django.db import models
from register.utils import *
from django.db import models

class ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    local = models.CharField(max_length=200)
    day = models.DateField()
    hour = models.TimeField()

    def __str__(self):
        return f'Evento de {self.event_name}'

    