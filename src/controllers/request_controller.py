# src/controllers/request_handler.py

import requests
from config import BASE_URL  # Import the globally defined BASE_URL
from fastapi import HTTPException


class Request:
    """
    A class to handle HTTP requests to the BASE_URL.
    """

    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint: str, params: dict = None):
        """Handles GET requests."""
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"GET request failed: {str(e)}")

    def post(self, endpoint: str, data: dict = None):
        """Handles POST requests."""
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=500, detail=f"POST request failed: {str(e)}"
            )

    def put(self, endpoint: str, data: dict = None):
        """Handles PUT requests."""
        try:
            response = requests.put(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"PUT request failed: {str(e)}")

    def delete(self, endpoint: str, params: dict = None):
        """Handles DELETE requests."""
        try:
            response = requests.delete(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=500, detail=f"DELETE request failed: {str(e)}"
            )
