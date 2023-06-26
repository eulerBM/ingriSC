from django.db import models
from django.contrib.auth.models import User

class ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    local = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __str__(self):
        return f'Evento de {self.event_name}'