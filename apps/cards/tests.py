from datetime import date, timedelta

from rest_framework.test import APITestCase

from .models import Card, Deck


class TestModel(APITestCase):
    def test_today_retrieve_cards_due_today(self):
        # Create a deck
        deck = Deck.objects.create(title="Test Deck")

        # Create a card due for review today
        card_due_today = Card.objects.create(
            deck=deck,
            question="Question 1",
            answer="Answer 1",
            next_review=date.today()
        )

        # Create a card not due for review today
        card_not_due_today = Card.objects.create(
            deck=deck,
            question="Question 2",
            answer="Answer 2",
            next_review=date.today() + timedelta(days=1)
        )

        # Call the today() method
        cards_due_today = Card.objects.today()

        # Assert that the card due today is in the result set
        assert card_due_today in cards_due_today

        # Assert that the card not due today is not in the result set
        assert card_not_due_today not in cards_due_today

    def test_today_with_additional_filters(self):
        # Create a deck
        deck = Deck.objects.create(title="Test Deck")

        # Create a card due for review today
        card_due_today = Card.objects.create(deck=deck, question="Question 1", answer="Answer 1",
                                             next_review=date.today())

        # Create a card not due for review today
        card_not_due_today = Card.objects.create(deck=deck, question="Question 2", answer="Answer 2",
                                                 next_review=date.today() + timedelta(days=1))

        # Call the today() method with additional filters
        cards_due_today = Card.objects.today().filter(deck=deck, bucket=1)

        # Assert that the card due today is in the result set
        assert card_due_today in cards_due_today

        # Assert that the card not due today is not in the result set
        assert card_not_due_today not in cards_due_today

    def test_returns_question_field(self):
        card = Card(question="What is the capital of Iran?")
        assert str(card) == "What is the capital of Iran?"

    def test_returns_string_with_length_greater_than_500(self):
        card = Card(question="A" * 501)
        assert len(str(card)) > 500
