from django.db import models


class Timestamp(models.Model):
    """
    Provides fields for tracking the creation and update times of our model classes objects.
    """
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_time']
