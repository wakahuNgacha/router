from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import *

# Create your views here.

class TruckListView(ListAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

class TruckCreateView(CreateAPIView):
    serializer_class = TruckCreateSerializer
    queryset = Truck.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class TruckDetailView(RetrieveAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()

class TruckUpdateView(UpdateAPIView):
    serializer_class = TruckUpdateSerializer
    queryset = Truck.objects.all()

    def perform_update(self, serializer):
        serializer.save()

class TruckDeleteView(DestroyAPIView):
    queryset = Truck.objects.all()
