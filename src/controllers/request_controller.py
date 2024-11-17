# src/controllers/request_handler.py
import requests
from config import BASE_URL  # Import the globally defined BASE_URL
from fastapi import HTTPException
from typing import Literal, TypedDict, Optional, Union, Dict

EndpointParam = Literal["server.api"]
MethodParam = Literal["food_entries.get.v2", "foods.search.v3"]
FormatParam = Literal["json"]


class RequestParams(TypedDict):
    method: MethodParam
    format: FormatParam
    search_expression: str


class Request:
    """
    A class to handle HTTP requests to the BASE_URL.
    """

    def __init__(self):
        self.base_url = BASE_URL

    _methods: list = ["food_entries.get.v2"]

    def get(
        self,
        endpoint: EndpointParam,
        params: Optional[Union[RequestParams, Dict[str, str]]] = None,
        headers: dict = None,
        debug: bool = False,
    ):
        """Handles GET requests."""
        response = requests.get(
            f"{self.base_url}/{endpoint}", params=params, headers=headers
        )

        if debug:
            print(f"[DEBUG] {response.url}")
            print(f"[DEBUG] {response.headers}")
            print(f"[DEBUG] {response.raw}")
            print(f"[DEBUG] {response.request}")

        response.raise_for_status()
        return response

    def post(self, endpoint: EndpointParam, data: dict = None, headers: dict = None):
        """Handles POST requests."""
        response = requests.post(
            f"{self.base_url}/{endpoint}", json=data, headers=headers
        )
        response.raise_for_status()
        return response

    def put(self, endpoint: EndpointParam, data: dict = None):
        """Handles PUT requests."""
        response = requests.put(f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response

    def delete(self, endpoint: EndpointParam, params: dict = None):
        """Handles DELETE requests."""
        response = requests.delete(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response
