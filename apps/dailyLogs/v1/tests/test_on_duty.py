from django.urls import reverse
from rest_framework import status
from apps.dailyLogs.v1.models import OffDuty
from .base import BaseLogTest

class OnDutyTests(BaseLogTest):

    def test_create_on_duty(self):
        url = reverse('on-duty-create')

        data = {
            "daily_log": self.daily_log.id,
            "driver": self.driver.id,
            "start": self.now,
            "stop": self.later,
            "location": "Warehouse",
            "notes": "Loading"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)