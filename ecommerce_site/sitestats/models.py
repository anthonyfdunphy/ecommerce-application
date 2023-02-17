from django.db import models
from django.utils import timezone

class SiteStats(models.Model):
    url = models.CharField(max_length=200, unique=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url

    class Meta:
        unique_together = ('url',)
        verbose_name = 'Webpage Views'
        verbose_name_plural = 'Webpage Views'
