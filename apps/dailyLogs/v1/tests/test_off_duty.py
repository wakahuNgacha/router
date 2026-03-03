from django.urls import reverse
from rest_framework import status
from apps.dailyLogs.v1.models import OffDuty
from .base import BaseLogTest


class OffDutyTests(BaseLogTest):

    def test_create_off_duty(self):
        url = reverse('off-duty-create')

        data = {
            "daily_log": self.daily_log.id,
            "driver": self.driver.id,
            "start": self.now,
            "stop": self.later,
            "location": "Rest Area",
            "notes": "Break"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
