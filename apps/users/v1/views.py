from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import *
from .models import *

# Create your views here.
class UserCreateView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class DriverListView(ListAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()