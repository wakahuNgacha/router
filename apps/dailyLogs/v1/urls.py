from django.urls import path

from .views import *

from django.urls import path
from .views import *

urlpatterns = [
    path('daily-logs/', DailyLogListView.as_view(), name='daily-log-list'),
    path('daily-logs/create/', DailyLogCreateView.as_view(), name='daily-log-create'),
    path('daily-logs/<int:pk>/', DailyLogDetailView.as_view(), name='daily-log-detail'),
    path('daily-logs/<int:pk>/update/', DailyLogUpdateView.as_view(), name='daily-log-update'),
    path('daily-logs/<int:pk>/delete/', DailyLogDeleteView.as_view(), name='daily-log-delete'),

    path('off-duty/', OffDutyListView.as_view(), name='off-duty-list'),
    path('off-duty/create/', OffDutyCreateView.as_view(), name='off-duty-create'),
    path('off-duty/<int:pk>/', OffDutyDetailView.as_view(), name='off-duty-detail'),
    path('off-duty/<int:pk>/update/', OffDutyUpdateView.as_view(), name='off-duty-update'),
    path('off-duty/<int:pk>/delete/', OffDutyDeleteView.as_view(), name='off-duty-delete'),



    path('sleeper-berth/', SleeperBerthListView.as_view(), name='sleeper-berth-list'),
    path('sleeper-berth/create/', SleeperBerthCreateView.as_view(), name='sleeper-berth-create'),
    path('sleeper-berth/<int:pk>/', SleeperBerthDetailView.as_view(), name='sleeper-berth-details'),
    path('sleeper-berth/<int:pk>/update/', SleeperBerthUpdateView.as_view(), name='sleeper-berth-update'),
    path('sleeper-berth/<int:pk>/delete/', SleeperBerthDeleteView.as_view(), name='sleeper-berth-delete'),


    path('driving/', DrivingListView.as_view(), name='driving-list'),
    path('driving/create/', DrivingCreateView.as_view(), name='driving-create'),
    path('driving/<int:pk>/', DrivingDetailView.as_view(), name='driving-details'),
    path('driving/<int:pk>/update/', DrivingUpdateView.as_view(), name='driving-update'),
    path('driving/<int:pk>/delete/', DrivingDeleteView.as_view(), name='driving-delete'),


    path('on-duty/', OnDutyListView.as_view(), name='on-duty-list'),
    path('on-duty/create/', OnDutyCreateView.as_view(), name='on-duty-create'),
    path('on-duty/<int:pk>/', OnDutyDetailView.as_view(), name='on-duty-details'),
    path('on-duty/<int:pk>/update/', OnDutyUpdateView.as_view(), name='on-duty-update'),
    path('on-duty/<int:pk>/delete/', OnDutyDeleteView.as_view(), name='on-duty-delete'),
]