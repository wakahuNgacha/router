from django.urls import path
from .views import *

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
