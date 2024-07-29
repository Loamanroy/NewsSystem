from django.db import models


class NewsSystem(models.Model):
    title = models.CharField(max_length=36)
    content = models.TextField(max_length=255, blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
