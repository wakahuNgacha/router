from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import *
from .models import *

# Create your views here.
class DailyLogListView(ListAPIView):
    serializer_class = DailyLogSerializer
    queryset = DailyLog.objects.all()

class DailyLogCreateView(CreateAPIView):
    serializer_class = DailyLogCreateSerializer
    queryset = DailyLog.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class DailyLogDetailView(RetrieveAPIView):
    serializer_class = DailyLogSerializer
    queryset = DailyLog.objects.all()

class DailyLogUpdateView(UpdateAPIView):
    serializer_class = DailyLogUpdateSerializer
    queryset = DailyLog.objects.all()

    def perform_update(self, serializer):
        serializer.save()

class DailyLogDeleteView(DestroyAPIView):
    queryset = DailyLog.objects.all()

class OffDutyListView(ListAPIView):
    serializer_class = OffDutySerializer
    queryset = OffDuty.objects.all

class OffDutyCreateView(CreateAPIView):
    serializer_class = OffDutyCreateSerializer
    queryset = OffDuty.objects.all()

class OffDutyDetailView(RetrieveAPIView):
    serializer_class = OffDutySerializer
    queryset = OffDuty.objects.all()

class OffDutyUpdateView(UpdateAPIView):
    serializer_class = OffDutyUpdateSerializer
    queryset = OffDuty.objects.all()

class OffDutyDeleteView(DestroyAPIView):
    queryset = OffDuty.objects.all()

class SleeperBerthListView(ListAPIView):
    serializer_class = SleeperBerthSerializer
    queryset = SleeperBerth.objects.all()

class SleeperBerthCreateView(CreateAPIView):
    serializer_class = SleeperBerthCreateSerializer
    queryset = SleeperBerth.objects.all()

class SleeperBerthDetailView(RetrieveAPIView):
    serializer_class = SleeperBerthSerializer
    queryset = SleeperBerth.objects.all()

class SleeperBerthUpdateView(UpdateAPIView):
    serializer_class = SleeperBerthUpdateSerializer
    queryset = SleeperBerth.objects.all()

class SleeperBerthDeleteView(DestroyAPIView):
    queryset = SleeperBerth.objects.all()
    
class DrivingListView(ListAPIView):
    serializer_class = DrivingSerializer
    queryset = Driving.objects.all()

class DrivingCreateView(CreateAPIView):
    serializer_class = DrivingCreateSerializer
    queryset = Driving.objects.all()

class DrivingDetailView(RetrieveAPIView):
    serializer_class = DrivingSerializer
    queryset = Driving.objects.all()

class DrivingUpdateView(UpdateAPIView):
    serializer_class = DrivingUpdateSerializer
    queryset = Driving.objects.all()

class DrivingDeleteView(DestroyAPIView):
    queryset = Driving.objects.all()

class OnDutyListView(ListAPIView):
    serializer_class = OnDutySerializer
    queryset = OnDuty.objects.all()

class OnDutyCreateView(CreateAPIView):
    serializer_class = OnDutyCreateSerializer
    queryset = OnDuty.objects.all()

class OnDutyDetailView(RetrieveAPIView):
    serializer_class = OnDutySerializer
    queryset = OnDuty.objects.all()

class OnDutyUpdateView(UpdateAPIView):
    serializer_class = OnDutyUpdateSerializer
    queryset = OnDuty.objects.all()

class OnDutyDeleteView(DestroyAPIView):
    queryset = OnDuty.objects.all()
