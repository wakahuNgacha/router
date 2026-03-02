from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from faker import Faker

from apps.companies.v1.models import Company

fake = Faker()

class CompanyAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Sample company data
        self.company_data = {
            "name": fake.company(),
            "address": fake.address(),
            "phone_number": fake.phone_number()
        }

    def test_create_company(self):
        url = reverse('company-create')
        response = self.client.post(url, self.company_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Company.objects.filter(name=self.company_data['name']).exists())

    def test_list_companies(self):
        # Create a company first
        Company.objects.create(**self.company_data)
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_company(self):
        company = Company.objects.create(**self.company_data)
        url = reverse('company-detail', kwargs={'pk': company.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], company.name)

    def test_update_company(self):
        company = Company.objects.create(**self.company_data)
        url = reverse('company-update', kwargs={'pk': company.id})
        updated_data = {"name": "Updated Company Name"}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        company.refresh_from_db()
        self.assertEqual(company.name, "Updated Company Name")

    def test_delete_company(self):
        company = Company.objects.create(**self.company_data)
        url = reverse('company-delete', kwargs={'pk': company.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Company.objects.filter(id=company.id).exists())
