from django.urls import reverse
from rest_framework import status
from datetime import date

from apps.dailyLogs.v1.models import DailyLog
from .base import BaseLogTest


class DailyLogTests(BaseLogTest):

    def test_create_daily_log(self):
        url = reverse('daily-log-create')

        data = {
            "date": str(date.today()),
            "driver": self.driver.id,
            "truck": self.truck.id,
            "route": self.route.id,
            "total_driving_milage": 250,
            "notes": "Test log"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DailyLog.objects.count(), 2)

    def test_list_daily_logs(self):
        url = reverse('daily-log-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_daily_log(self):
        url = reverse('daily-log-update', kwargs={"pk": self.daily_log.id})

        response = self.client.put(url, {
            "date": str(date.today()),
            "driver": self.driver.id,
            "truck": self.truck.id,
            "route": self.route.id,
            "total_driving_milage": 500
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_daily_log(self):
        url = reverse('daily-log-delete', kwargs={"pk": self.daily_log.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DailyLog.objects.count(), 0)
