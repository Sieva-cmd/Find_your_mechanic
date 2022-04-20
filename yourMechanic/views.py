from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  FullBodyPaint, StereoSetup,EngineRepair,Customer,Mechanic
from .serializer import FullBodyPaintSerializer,StereoSetupSerializer,EngineRepairSerializer,CustomerSerializer,MechanicSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# Create your views here.

class FullBodyPaintList(APIView):
    def get(self, request, format=None):
        paint = FullBodyPaint.objects.all()
        serializers = FullBodyPaintSerializer(paint, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = FullBodyPaintSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class StereoSetupList(APIView):
    def get(self, request, format=None):
        stereo = StereoSetup.objects.all()
        serializers = StereoSetupSerializer(stereo, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = StereoSetupSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class EngineRepairList(APIView):
    def get(self, request, format=None):
        engine = EngineRepair.objects.all()
        serializers = EngineRepairSerializer(engine, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = EngineRepairSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class CustomerList(APIView):
    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializers = CustomerSerializer(customer, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class MechanicList(APIView):
    def get(self, request, format=None):
        mechanic = Mechanic.objects.all()
        serializers = MechanicSerializer(mechanic, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = MechanicSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

