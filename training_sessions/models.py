from django.db import models
from general.models import Coach, Athlete

class TrainingSession(models.Model):

    date = models.DateField()
    hour = models.TimeField()
    capacity = models.IntegerField()
    coach = models.ManyToManyField(Coach, related_name='coaches')
    athletes = models.ManyToManyField(Athlete, related_name='athletes')

    def __str__(self) -> str:
        # return f"Training session ID {id} on {date} at {hour} with {capacity} people at max."
        return f"Training session ID {id}"