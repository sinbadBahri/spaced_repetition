from datetime import date
from django.contrib import admin
from .models import Card


@admin.action(description="Mark selected items as todays cards")
def make_today(modeladmin, request, queryset):
    today = date.today()
    queryset.update(next_review=today)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_select_related = ['deck']
    list_display = ['id', 'question', 'deck', 'next_review', 'last_reviewed']
    list_display_links = ['id', 'question']
    list_filter = ['deck', 'bucket']
    list_per_page = 10
    search_fields = ['question', 'answer', 'deck__title', 'deck__description']
    search_help_text = """
    Search a part of a cards Question or Answer, 
     You can also search the decks name or a part its description, 
     which this card is related to ..."""

    save_as = True
    actions = [make_today]
