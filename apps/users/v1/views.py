from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import *
from .models import *
# Create your views here.
class UserListView(ListAPIView):
    pass

class UserDetailView(RetrieveAPIView):
    pass

class UserCreateView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class UserUpdateView(UpdateAPIView):
    pass