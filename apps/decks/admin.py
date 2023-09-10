from django.contrib import admin
from .models import Deck
from ..cards.models import Card

class CardInline(admin.TabularInline):
    """
    This class helps you to create new cards inside a deck settings which are related to the same deck.
    """
    model = Card
    extra = 2
    can_delete = True


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['id' ,'title', 'last_reviewed']
    list_display_links = ['id', 'title']
    search_fields = ['search', 'description']
    search_help_text = """
    Search decks names or a part of their description..."""
    list_per_page = 10
    inlines = [CardInline]
