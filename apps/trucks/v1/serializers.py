from rest_framework import serializers
from apps.companies.v1.models import Company
from apps.trucks.v1.models import Truck
from apps.users.v1.models import Driver

class TruckSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all())

    class Meta:
        model = Truck
        fields = '__all__'

class TruckListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'license_plate', 'company', 'driver']

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
