from django.db import models
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
