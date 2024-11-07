from django.shortcuts import render
from rest_framework import generics
from .serializers import CardSerializer
from .models import Card

class CardView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer