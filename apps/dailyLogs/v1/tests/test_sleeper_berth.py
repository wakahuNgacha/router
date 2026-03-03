from django.urls import reverse
from rest_framework import status
from apps.dailyLogs.v1.models import OffDuty
from .base import BaseLogTest

class SleeperBerthTests(BaseLogTest):

    def test_create_sleeper_berth(self):
        url = reverse('sleeper-berth-create')

        data = {
            "daily_log": self.daily_log.id,
            "driver": self.driver.id,
            "start": self.now,
            "stop": self.later,
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
