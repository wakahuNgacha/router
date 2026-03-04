from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from faker import Faker

from apps.trucks.v1.models import Truck
from apps.companies.v1.serializers import CompanyCreateSerializer
from apps.companies.v1.models import Company

fake = Faker()

class TruckAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a company instance
        company_data = {
            "name": fake.company(),
            "address": fake.address(),
            "phone_number": "+254113292165"
        }

        serializer = CompanyCreateSerializer(data=company_data)
        serializer.is_valid(raise_exception=True)
        self.company = serializer.save()

        self.truck_data = {
            "license_plate": fake.license_plate(),
            "model": fake.word(),
            "consumption": 8.5,
            "max_range": 400,
            "capacity": 12.5,
            "company": self.company,
            "total_truck_milage": 1200
        }

        self.data = {
            "license_plate": fake.license_plate(),
            "model": fake.word(),
            "consumption": 8.5,
            "max_range": 400,
            "capacity": 12.5,
            "company": self.company.id,
            "total_truck_milage": 1200
        }

    def test_create_truck(self):
        url = reverse('truck-create')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_trucks(self):
        Truck.objects.create(**self.truck_data)
        url = reverse('truck-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_truck(self):
        truck = Truck.objects.create(**self.truck_data)
        url = reverse('truck-update', kwargs={'pk': truck.id})
        updated_data = {"model": "UpdatedModel"}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        truck.refresh_from_db()
        self.assertEqual(truck.model, "UpdatedModel")

    def test_delete_truck(self):
        truck = Truck.objects.create(**self.truck_data)
        url = reverse('truck-delete', kwargs={'pk': truck.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Truck.objects.filter(id=truck.id).exists())

    def test_create_truck_without_company_fails(self):
        invalid_data = self.truck_data.copy()
        invalid_data.pop("company")
        url = reverse('truck-create')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
