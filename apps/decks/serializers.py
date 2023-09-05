from rest_framework import serializers
from .models import Deck


class DeckSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Deck
        fields = ('id', 'title', 'description',
                  'created_time', 'updated_time')
