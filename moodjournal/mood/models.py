from django.db import models

# Create your models here.


class Mood(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return '%s' % (self.name)
