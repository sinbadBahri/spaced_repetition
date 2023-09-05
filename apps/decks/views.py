from rest_framework import viewsets
from rest_framework.response import Response

from .models import Deck
from .serializers import DeckSerializer

from ..cards.models import Card
from ..cards.serializers import CardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckCardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk) -> Response:
        queryset = Card.objects.filter(deck_id=decks_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)


class TodayCardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk) -> Response:
        queryset = Card.objects.today().filter(deck_id=decks_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)
