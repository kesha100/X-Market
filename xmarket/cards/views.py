from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer
# Create your views here.


class CardListAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer