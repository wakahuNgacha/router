from apps.routes.v1.models import Route
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from django.conf import settings


class GetRouteeService:

    def __init__(self):
        self.url = settings.OPENROUTSERVICE_URL
        self.token = settings.OPENROUTSERVICE_TOKEN

        if not self.url or not self.token:
            raise ValueError("OpenRouteeService credentials not configured properly.")

    def fetch_routee(self, origin_lat, origin_lng, dest_lat, dest_lng):

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
        }

        payload = {
            "coordinates": [
                [origin_lng, origin_lat],
                [dest_lng, dest_lat],
            ]
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Error calling OpenRouteeService: {str(e)}")

        data = response.json()

        return data
