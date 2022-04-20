from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  FullBodyPaint, StereoSetup
from .serializer import FullBodyPaintSerializer,StereoSetupSerializer
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