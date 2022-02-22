from django.db import models
from apps.utils.models import Timestamps


class Waitlist(Timestamps, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    level = models.IntegerField(verbose_name="Class Level", default=1)
    notes = models.TextField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
