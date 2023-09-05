from django.db import models
from django.db.models import CharField
from ..helpers.models import Timestamp


class Deck(Timestamp):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    last_reviewed = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> CharField:
        return self.title
