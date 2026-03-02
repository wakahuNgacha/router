from rest_framework import serializers
from apps.routes.v1.models import Route
from apps.routes.v1.serializers import RouteSerializer
from apps.trucks.v1.models import Truck
from apps.trucks.v1.serializers import TruckSerializer
from apps.users.v1.models import Driver
from apps.dailyLogs.v1.models import *
from apps.users.v1.serializers import DriverSerializer

class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class DailyLogListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = ['id', 'truck', 'route', 'date']

class DailyLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class DailyLogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class DailyLogDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class DailyLogDetailSerializer(serializers.ModelSerializer):
    truck = TruckSerializer()
    route = RouteSerializer()
    driver = DriverSerializer()

    class Meta:
        model = DailyLog
        fields = '__all__'

class OffDutySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class OffDutyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class OffDutyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class OffDutyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class SleeperBerthSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class SleeperBerthCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class SleeperBerthUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class SleeperBerthDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class DrivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class DrivingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driving
        fields = '__all__'

class DrivingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driving
        fields = '__all__'

class DrivingDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driving
        fields = '__all__'

class OnDutySerializer(serializers.ModelSerializer):
    class Meta:
        model = OnDuty
        fields = '__all__'

class OnDutyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnDuty
        fields = '__all__'

class OnDutyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnDuty
        fields = '__all__'

class OnDutyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnDuty
        fields = '__all__'


