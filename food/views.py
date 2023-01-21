from django.shortcuts import render
from rest_framework import generics
from .models import Food
from .serializer import FoodSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class FoodList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
