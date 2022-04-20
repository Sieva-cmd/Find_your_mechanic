from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  FullBodyPaint
from .serializer import FullBodyPaintSerializer

# Create your views here.

class FullBodyPaintList(APIView):
    def get(self, request, format=None):
        paint = FullBodyPaint.objects.all()
        serializers = FullBodyPaintSerializer(paint, many=True)
        return Response(serializers.data)
