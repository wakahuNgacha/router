from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker
from apps.users.v1.models import User

fake = Faker()


class AuthAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.register_url = reverse('user_register')
        self.token_url = reverse('token_obtain')
        self.refresh_url = reverse('token_refresh')

        self.password = "StrongPass123!"

        self.user_data = {
            "email": fake.email(),
            "username": fake.user_name(),
            "password": self.password,
            "role": "driver"
        }

    def test_user_registration_success(self):
        response = self.client.post(self.register_url, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=self.user_data["email"]).exists())

    def test_user_registration_duplicate_email(self):
        User.objects.create_user(
            email=self.user_data["email"],
            username=self.user_data["username"],
            password=self.password
        )

        response = self.client.post(self.register_url, self.user_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_obtain_success(self):
        User.objects.create_user(
            email=self.user_data["email"],
            username=self.user_data["username"],
            password=self.password
        )

        response = self.client.post(self.token_url, {
            "email": self.user_data["email"],
            "password": self.password
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_token_refresh(self):
        user = User.objects.create_user(
            email=self.user_data["email"],
            username=self.user_data["username"],
            password=self.password
        )

        token_response = self.client.post(self.token_url, {
            "email": self.user_data["email"],
            "password": self.password
        }, format='json')

        refresh_token = token_response.data["refresh"]

        response = self.client.post(self.refresh_url, {
            "refresh": refresh_token
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_default_role_is_driver(self):
        user = User.objects.create_user(
            email=fake.email(),
            username=fake.user_name(),
            password=self.password
        )

        self.assertEqual(user.role, "driver")
