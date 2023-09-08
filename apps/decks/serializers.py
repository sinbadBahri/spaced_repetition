from rest_framework import serializers
from .models import Deck


class DeckSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert the Deck model instances into JSON format
    """

    class Meta:
        model = Deck
        fields = ('id', 'title', 'description',
                  'created_time', 'updated_time')
