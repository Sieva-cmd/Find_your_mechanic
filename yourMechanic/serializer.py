from rest_framework import serializers
from .models import FullBodyPaint,StereoSetup,EngineRepair, Customer,Mechanic

class FullBodyPaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullBodyPaint
        fields = ('user', 'part', 'mechanic','description', 'price')

class StereoSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StereoSetup
        fields = ('user', 'part','description', 'price')

class EngineRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineRepair
        fields = ('user', 'part','description', 'price')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'description', 'price')

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ('name', 'description', 'price')