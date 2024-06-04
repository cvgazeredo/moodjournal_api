from django.db import models
from mood.models import Mood
from patient.models import Patient
from django.utils import timezone

# Create your models here.


class Journal(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='journal', on_delete=models.CASCADE)
    text = models.TextField()
    mood = models.ForeignKey(Mood, related_name='journal',
                             null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return '%s', '%s', '%s', '%s' % (self.text, self.mood, self.patient, self.created_at)
