from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView

from apps.companies.v1.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
