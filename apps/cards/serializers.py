from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    """
    Converts Card model instances into JSON format.
    """

    class Meta:
        model = Card
        fields = ('id', 'question', 'answer',
                  'deck', 'bucket', 'last_reviewed',
                  'created_time', 'updated_time')
