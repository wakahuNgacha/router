from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView

from apps.routs.v1.models import Rout
from .serializers import *

# Create your views here.
class RoutListView(ListAPIView):
    serializer_class = RoutSerializer
    queryset = Rout.objects.all()

class RoutCreateView(CreateAPIView):
    serializer_class = RoutCreateSerializer
    queryset = Rout.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class RoutDetailView(RetrieveAPIView):
    serializer_class = RoutSerializer
    queryset = Rout.objects.all()

class RoutUpdateView(UpdateAPIView):
    serializer_class = RoutUpdateSerializer
    queryset = Rout.objects.all()

    def perform_update(self, serializer):
        serializer.save()

class RoutDeleteView(DestroyAPIView):
    queryset = Rout.objects.all()
