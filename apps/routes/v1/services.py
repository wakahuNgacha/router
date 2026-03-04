from apps.routes.v1.models import Route
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from django.conf import settings
import pandas as pd
from geopy.distance import geodesic
from apps.trucks.v1.models import Truck


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

class GetFuelingStations:

    TARGET_MILES = 500
    SEARCH_RADIUS_MILES = 10

    def __init__(self, route_response):
        """
        route_response = full JSON response from OpenRouteService
        """
        self.route_response = route_response
        self.csv_path = settings.FUEL_STATIONS_CSV_PATH

    def get_500_mile_coordinate(self):
        """
        Walk through route geometry and return coordinate
        near 500 miles from origin.
        """
        coords = self.route_response["features"][0]["geometry"]["coordinates"]

        target_meters = self.TARGET_MILES * 1609.34
        cumulative_distance = 0

        for i in range(len(coords) - 1):
            p1 = (coords[i][1], coords[i][0])     # (lat, lng)
            p2 = (coords[i + 1][1], coords[i + 1][0])

            segment_distance = geodesic(p1, p2).meters
            cumulative_distance += segment_distance

            if cumulative_distance >= target_meters:
                return p2

        return None  # route shorter than 500 miles

    def find_nearby_stations(self, checkpoint):
        df = pd.read_csv(self.csv_path)

        df.columns = df.columns.str.strip()

        df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
        df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

        df = df.dropna(subset=["Latitude", "Longitude"])

        nearby = []

        for _, row in df.iterrows():
            station = (row["Latitude"], row["Longitude"])
            distance = geodesic(checkpoint, station).miles

            if distance <= self.SEARCH_RADIUS_MILES:
                nearby.append({
                    "Truckstop Name": row.get("TruckstopName"),
                    "Latitude": row["Latitude"],
                    "Longitude": row["Longitude"],
                    "Retail Price": row.get("Retail Price"),
                    "distance_from_checkpoint_miles": round(distance, 2),
                })

        return nearby

    def get_fueling_stations(self):
        checkpoint = self.get_500_mile_coordinate()

        fueling_stations = self.find_nearby_stations(checkpoint)

        return fueling_stations
    
    def get_fuel_price(self, fueling_stations):
        if not fueling_stations:
            return 0

        prices = [
            station.get("Retail Price")
            for station in fueling_stations
            if station.get("Retail Price") is not None
        ]

        if not prices:
            return 0

        cheapest_price = min(prices)

        capacity = 50

        fuel_cost = cheapest_price * capacity

        return round(fuel_cost, 2)

