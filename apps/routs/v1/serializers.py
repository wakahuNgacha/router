from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.routs.v1.models import Rout
from apps.routs.v1.services import *

class RoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'

class RoutListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = ['id', 'name']

# should be within the USA
# class RoutCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rout
#         fields = "__all__"
class RoutCreateSerializer(serializers.ModelSerializer):
    route_data = serializers.SerializerMethodField()  # Optional: include full API response

    class Meta:
        model = Rout
        fields = "__all__"

    def get_route_data(self, obj):
        return getattr(obj, "_route_data", None)

    def create(self, validated_data):
        instance = Rout.objects.create(**validated_data)

        service = GetRouteService()
        route_response = service.fetch_route(
            origin_lat=instance.origin_lat,
            origin_lng=instance.origin_lng,
            dest_lat=instance.destination_lat,
            dest_lng=instance.destination_lng,
        )

        instance._route_data = route_response

        return instance
    
class RoutUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'

class RoutDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rout
        fields = '__all__'
