from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView

from apps.routes.v1.models import Route
from .serializers import *

# Create your views here.
class RouteListView(ListAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

class RouteCreateView(CreateAPIView):
    serializer_class = RouteCreateSerializer
    queryset = Route.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class RouteDetailView(RetrieveAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

class RouteUpdateView(UpdateAPIView):
    serializer_class = RouteUpdateSerializer
    queryset = Route.objects.all()

    def perform_update(self, serializer):
        serializer.save()

class RouteDeleteView(DestroyAPIView):
    queryset = Route.objects.all()
