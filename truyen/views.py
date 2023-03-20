from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Truyen
from .serializers import TruyebSerializer


# Create your views here.

class TruyenApiView(generics.ListCreateAPIView):
    queryset = Truyen.objects.filter(removed=False)
    serializer_class = TruyebSerializer

    def get(self, request):
        obj = Truyen.objects.filter(removed=False)
        obj.views = obj.views + 1
        obj.save()
        serializer = TruyebSerializer(obj, many=True)
        return Response(serializer.data, status=200)
