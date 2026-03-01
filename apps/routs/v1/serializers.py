from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.routs.v1.models import Rout

class RoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'

class RoutListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = ['id', 'name']

class RoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'

class RoutUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'

class RoutDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'
