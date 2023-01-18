from django.shortcuts import render
from rest_framework import generics
from .models import Food
from .serializer import FoodSerializer


# Create your views here.
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
