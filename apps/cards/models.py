from django.db import models
from django.db.models import TextField

from ..helpers.models import Timestamp
from ..decks.models import Deck

from datetime import date


class MyManager(models.Manager):
    """
    MyManager overrides the get_queryset() method to include a select_related() call to efficiently retrieve related
    Deck objects and reduces the number of reads in Queries.
    It also has the method, today(), that retrieves cards that are due for review today.
    """
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).select_related('deck')

    def today(self, *args, **kwargs):
        today = date.today()
        return super().get_queryset(*args, **kwargs).filter(next_review__day=today.day)


class Card(Timestamp):
    """
    The Card class represents a flashcard and is related to a Deck through a foreign key relationship.
    It has fields for the question, answer, bucket (representing the review interval), and timestamps for when
    the card was last reviewed and when it is next due for review.
    It inherits from the Timestamp model, which provides fields for created and updated timestamps.
    It defines a custom manager MyManager that adds a method today() to retrieve cards that are due for review today.
    """
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    buckets = (
        (1, '1 Day'),
        (2, '3 Days'),
        (3, '7 Days'),
        (4, '16 Days'),
        (5, '30 Days'),
    )
    bucket = models.IntegerField(choices=buckets, default=1)
    last_reviewed = models.DateTimeField(auto_now_add=True)
    next_review = models.DateTimeField(blank=True, null=True)

    default_manager = models.Manager()
    objects = MyManager()

    def __str__(self) -> TextField:
        return self.question
