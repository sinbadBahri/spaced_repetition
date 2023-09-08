from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card


class CardViewSet(viewsets.ModelViewSet):
    """
     A viewset that provides CRUD operations for the Card model.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
