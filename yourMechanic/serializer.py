from rest_framework import serializers
from .models import FullBodyPaint

class FullBodyPaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullBodyPaint
        fields = ('user', 'part', 'description', 'mechanic', 'price')