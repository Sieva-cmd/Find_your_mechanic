from rest_framework import serializers
from .models import FullBodyPaint,StereoSetup

class FullBodyPaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullBodyPaint
        fields = ('user', 'part', 'mechanic','description', 'price')

class StereoSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StereoSetup
        fields = ('user', 'part','description', 'price')