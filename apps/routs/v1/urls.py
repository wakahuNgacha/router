from django.urls import path
from .views import *

urlpatterns = [
    path('routs/', RoutListView.as_view(), name='rout-list'),
    path('routs/create/', RoutCreateView.as_view(), name='rout-create'),
    path('routs/<int:pk>/', RoutDetailView.as_view(), name='rout-detail'),
    path('routs/<int:pk>/update/', RoutUpdateView.as_view(), name='rout-update'),
]
