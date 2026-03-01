from django.urls import path
from .views import *

urlpatterns = [
    path('trucks/', TruckListView.as_view(), name='truck-list'),
    path('trucks/create/', TruckCreateView.as_view(), name='truck-create'),
    path('trucks/<int:pk>/', TruckDetailView.as_view(), name='truck-detail'),
    path('trucks/<int:pk>/update/', TruckUpdateView.as_view(), name='truck-update'),
    path('trucks/<int:pk>/delete/', TruckDeleteView.as_view(), name='truck-delete'),
]
