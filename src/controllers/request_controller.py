# src/controllers/request_handler.py

import requests
from config import BASE_URL  # Import the globally defined BASE_URL
from fastapi import HTTPException
from typing import Literal


class Request:
    """
    A class to handle HTTP requests to the BASE_URL.
    """

    def __init__(self):
        self.base_url = BASE_URL

    _methods: list = ["food_entries.get.v2"]

    EndpointType = Literal["food_entries.get.v2"]

    def get(self, endpoint: EndpointType, params: dict = None):
        """Handles GET requests."""
        try:
            response = requests.get(f"{self.base_url}?method={endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"GET request failed: {str(e)}")

    def post(self, endpoint: EndpointType, data: dict = None):
        """Handles POST requests."""
        try:
            response = requests.post(f"{self.base_url}?method={endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=500, detail=f"POST request failed: {str(e)}"
            )

    def put(self, endpoint: EndpointType, data: dict = None):
        """Handles PUT requests."""
        try:
            response = requests.put(f"{self.base_url}?method={endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"PUT request failed: {str(e)}")

    def delete(self, endpoint: EndpointType, params: dict = None):
        """Handles DELETE requests."""
        try:
            response = requests.delete(
                f"{self.base_url}?method={endpoint}", params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=500, detail=f"DELETE request failed: {str(e)}"
            )
