from django.conf import settings
from django.db import models
from django.utils import timezone

class Voetballers(models.Model):
    naam_voetballer = models.CharField(max_length=200)
    actuele_voetbalclub = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.naam_voetballer