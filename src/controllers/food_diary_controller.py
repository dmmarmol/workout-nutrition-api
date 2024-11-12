# src/controllers/fatsecret_controller.py

import requests
from fastapi import HTTPException
from .request_controller import Request


class FoodDiaryController:
    def __init__(self):
        self.request = Request()

    async def get_entries(self, date):
        """Fetch daily food entries for a given date."""
        params = {
            "date": date,
            "format": "json",
        }

        return self.request.get(endpoint="food_entries.get.v2", params=params)
