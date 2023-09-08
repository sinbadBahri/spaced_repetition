from rest_framework_nested import routers
from django.urls import path, include
from .views import DeckViewSet, DeckCardsViewSet, TodayCardsViewSet

app_name = 'decks'

router = routers.SimpleRouter()
router.register(prefix=r'', viewset=DeckViewSet, basename='decks_list')

cards_router = routers.NestedSimpleRouter(router, parent_prefix=r'', lookup='decks')
cards_router.register(prefix=r'cards', viewset=DeckCardsViewSet, basename='deck_cards')

today_cards_router = routers.NestedSimpleRouter(router, parent_prefix=r'', lookup='decks')
today_cards_router.register(r'today-cards', TodayCardsViewSet, basename='today_deck_cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
    path('', include(today_cards_router.urls)),
]
