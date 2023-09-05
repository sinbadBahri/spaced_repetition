from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
