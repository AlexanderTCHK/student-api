from math import degrees
from django.db import models
from apps.utils.models import Timestamps


class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecture_name = models.CharField(max_length=100, default="", blank=True)
    date = models.DateField()
    slides_url = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Enter number of hours")
    is_required = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
