from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'purchaser', 'type', 'description', 'created_at', 'updated_at')
        model = Food
