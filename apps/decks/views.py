from rest_framework import viewsets
from rest_framework.response import Response

from .models import Deck
from .serializers import DeckSerializer

from ..cards.models import Card
from ..cards.serializers import CardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations by using the DeckSerializer class to serialize and deserialize the data
    and CRUD the Deck class.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class DeckCardsViewSet(viewsets.ViewSet):
    """
    Handles the API endpoint for retrieving a list of cards associated with a specific deck.
    """

    def list(self, request, decks_pk) -> Response:
        """
        Retrieves a list of cards associated with a specific deck.
        """
        queryset = Card.objects.filter(deck_id=decks_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)


class TodayCardsViewSet(viewsets.ViewSet):
    """
    Handles the retrieval of flashcards that are due for review today.
    """

    def list(self, request, decks_pk) -> Response:
        """
        Retrieves the flashcards due for review today for the specified deck.

        decks_pk: The primary key of the deck for which to retrieve flashcards due for review today.
        """
        queryset = Card.objects.today().filter(deck_id=decks_pk)
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)
