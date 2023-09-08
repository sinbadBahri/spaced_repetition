from rest_framework.test import APITestCase

from .models import Deck
from .views import TodayCardsViewSet

from ..cards.models import Card


class TestModel(APITestCase):
    def test_return_title_as_string(self):
        deck = Deck(title="my Deck")
        assert str(deck) == "my Deck"

    def test_retrieve_all_decks(self):
        response = self.client.get('/api/v1/decks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Deck.objects.count())

    def test_retrieve_cards_with_valid_deck_id(self):
        # Create a valid deck
        deck = Deck.objects.create(title="Test Deck", description="It's about testing :)")

        # Create multiple cards associated with the deck
        card1 = Card.objects.create(deck=deck, question="Question 1", answer="Answer 1")
        card2 = Card.objects.create(deck=deck, question="Question 2", answer="Answer 2")

        # Make a request to the viewset with the valid deck ID
        response = self.client.get(f"/api/v1/decks/{deck.id}/cards/")

        # Assert that the response status code is 200
        assert response.status_code == 200

        # Assert that the response data contains the correct number of cards
        assert len(response.data) == 2

        # Assert that the response data contains the correct card details
        assert response.data[1]["question"] == "Question 1"
        assert response.data[1]["answer"] == "Answer 1"
        assert response.data[0]["question"] == "Question 2"
        assert response.data[0]["answer"] == "Answer 2"

    def test_retrieve_cards_with_empty_queryset(self):
        # Create a valid deck
        deck = Deck.objects.create(title="Test Deck", description="It's about testing :)")

        # Make a request to the viewset with the valid deck ID
        response = self.client.get(f"/api/v1/decks/{deck.id}/cards/")

        # Assert that the response status code is 200
        assert response.status_code == 200

        # Assert that the response data is an empty list
        assert response.data == []

    def test_no_flashcards_due_for_review_today(self):
        # Create a deck
        deck = Deck.objects.create(title="Test Deck", description="It's about testing :)")

        # Call the list method of TodayCardsViewSet
        response = TodayCardsViewSet().list(request=None, decks_pk=deck.pk)

        # Check that the response is empty
        assert response.status_code == 200
        assert response.data == []
