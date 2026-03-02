from django.urls import path
from .views import *

urlpatterns = [
    path('routes/', RouteListView.as_view(), name='route-list'),
    path('routes/create/', RouteCreateView.as_view(), name='route-create'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route-detail'),
    path('routes/<int:pk>/update/', RouteUpdateView.as_view(), name='route-update'),
]
