from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('id', 'question', 'answer',
                  'deck', 'bucket', 'last_reviewed',
                  'created_time', 'updated_time')
