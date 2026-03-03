from django.urls import reverse

from apps.dailyLogs.v1.models import DailyLog
from .base import BaseLogTest

class DrivingTests(BaseLogTest):

    def test_create_driving(self):
        url = reverse('driving-create')

        data = {
            "daily_log": self.daily_log.id,
            "driver": self.driver.id,
            "start": self.now,
            "stop": self.later
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
