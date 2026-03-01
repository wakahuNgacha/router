from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from apps.companies.v1.models import Company

# Create your views here.   
class CompanyListView(ListAPIView):
    serializer_class = CompanyListViewSerializer
    queryset = Company.objects.all()

class CompanyCreateView(CreateAPIView):
    serializer_class = CompanyCreateSerializer
    queryset = Company.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class CompanyDetailView(RetrieveAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class CompanyUpdateView(UpdateAPIView):
    serializer_class = CompanyCreateSerializer
    queryset = Company.objects.all()

    def perform_update(self, serializer):
        serializer.save()

class CompanyDeleteView(DestroyAPIView):
    queryset = Company.objects.all()
