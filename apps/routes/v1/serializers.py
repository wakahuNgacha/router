from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.routes.v1.models import Route
from apps.routes.v1.services import *

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class RouteListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name']

class RouteCreateSerializer(serializers.ModelSerializer):
    routee_data = serializers.SerializerMethodField()  # Optional: include full API response

    class Meta:
        model = Route
        fields = "__all__"

    def get_routee_data(self, obj):
        return getattr(obj, "_routee_data", None)

    def create(self, validated_data):
        instance = Route.objects.create(**validated_data)

        service = GetRouteeService()
        routee_response = service.fetch_routee(
            origin_lat=instance.origin_lat,
            origin_lng=instance.origin_lng,
            dest_lat=instance.destination_lat,
            dest_lng=instance.destination_lng,
        )
        
        instance.routees = routee_response.get("routees", [])
        instance.save()

        return instance
    
class RouteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class RouteDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
