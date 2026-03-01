from django.urls import path

from .views import *

from django.urls import path
from .views import *

urlpatterns = [
    path('daily-logs/', DailyLogListView.as_view()),
    path('daily-logs/create/', DailyLogCreateView.as_view()),
    path('daily-logs/<int:pk>/', DailyLogDetailView.as_view()),
    path('daily-logs/<int:pk>/update/', DailyLogUpdateView.as_view()),
    path('daily-logs/<int:pk>/delete/', DailyLogDeleteView.as_view()),


    path('off-duty/', OffDutyListView.as_view()),
    path('off-duty/create/', OffDutyCreateView.as_view()),
    path('off-duty/<int:pk>/', OffDutyDetailView.as_view()),
    path('off-duty/<int:pk>/update/', OffDutyUpdateView.as_view()),
    path('off-duty/<int:pk>/delete/', OffDutyDeleteView.as_view()),


    path('sleeper-berth/', SleeperBerthListView.as_view()),
    path('sleeper-berth/create/', SleeperBerthCreateView.as_view()),
    path('sleeper-berth/<int:pk>/', SleeperBerthDetailView.as_view()),
    path('sleeper-berth/<int:pk>/update/', SleeperBerthUpdateView.as_view()),
    path('sleeper-berth/<int:pk>/delete/', SleeperBerthDeleteView.as_view()),


    path('driving/', DrivingListView.as_view()),
    path('driving/create/', DrivingCreateView.as_view()),
    path('driving/<int:pk>/', DrivingDetailView.as_view()),
    path('driving/<int:pk>/update/', DrivingUpdateView.as_view()),
    path('driving/<int:pk>/delete/', DrivingDeleteView.as_view()),


    path('on-duty/', OnDutyListView.as_view()),
    path('on-duty/create/', OnDutyCreateView.as_view()),
    path('on-duty/<int:pk>/', OnDutyDetailView.as_view()),
    path('on-duty/<int:pk>/update/', OnDutyUpdateView.as_view()),
    path('on-duty/<int:pk>/delete/', OnDutyDeleteView.as_view()),
]