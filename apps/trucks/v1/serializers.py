from rest_framework import serializers
from apps.companies.v1.models import Company
from apps.trucks.v1.models import Truck

class TruckSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())


    class Meta:
        model = Truck
        fields = '__all__'

class TruckListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'license_plate', 'company']

class TruckCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class TruckUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class TruckDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'
