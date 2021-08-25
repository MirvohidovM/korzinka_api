from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Mahsulotlar
from .serializers import MahsulotlarSerializer


class MahsulotlarViewset(ModelViewSet):
    queryset = Mahsulotlar.objects.all()
    serializer_class = MahsulotlarSerializer
    permission_classes = (permissions.IsAuthenticated,)