from django.shortcuts import render

from rest_framework import viewsets, generics

from .serializers import QueueSerializer, MakananSerializer, MerchantSerializer, QuotesSerializer
from antrian.models import Queue
from merchant.models import Makanan, Merchant
from login.models import quotes

class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer


class MakananViewSet(viewsets.ModelViewSet):
    queryset = Makanan.objects.all()
    serializer_class = MakananSerializer


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class QuotesViewSet(viewsets.ModelViewSet):
    queryset = quotes.objects.all()
    serializer_class = QuotesSerializer


