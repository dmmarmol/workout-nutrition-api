import time
from config import BASE_URL, API_CLIENT_ID, API_CLIENT_SECRET
from .request_controller import Request, MethodParam, RequestParams
from requests import Response, exceptions, post, auth
from .utils_controller import Utils


class FatSecretController:
    def __init__(self):
        self._client_id: str = API_CLIENT_ID
        self._client_secret: str = API_CLIENT_SECRET
        self._access_token: str = None
        self._expires_in: int = 0

        self._get_access_token()

    def _get_access_token(self):
        """Request a new access token if the current one is expired or not set."""
        is_token_expired = time.time() >= self._expires_in
        # Token exist
        if self._access_token and is_token_expired is False:
            Utils.debug("Auth token exist. Skiping.")
            return

        # Token don't exist or is already expired
        if self._access_token is None or is_token_expired:

            try:
                Utils.debug("Trying to get auth token...")
                #
                # Using native python request.post method
                # to avoid dealing with a different BASE_URL for this request
                #
                response = post(
                    "https://oauth.fatsecret.com/connect/token",
                    headers={
                        "content-type": "application/x-www-form-urlencoded",
                    },
                    data={"grant_type": "client_credentials", "scope": "premier"},
                    auth=auth.HTTPBasicAuth(API_CLIENT_ID, API_CLIENT_SECRET),
                )
                response.raise_for_status()

                Utils.debug(
                    f"Auth was successful. Response stauts is: {response.status_code}"
                )

                json_response = response.json()
                access_token = json_response.get("access_token")
                expires_in = json_response.get("expires_in")

                Utils.debug(f"New access token: {access_token}")
                self._access_token = access_token
                self._expires_in = time.time() + expires_in
            except exceptions.HTTPError as e:
                error_detail = f"Failed to authenticate. Status Code: {e.response.status_code}, Response: {e.response.text}"
                raise ValueError(error_detail) from e

    def _get_auth_headers(self):
        Utils.debug("Creating auth headers...")
        self._get_access_token()

        if self._access_token is None:
            raise ValueError("An access token is required for this type of request.")

        headers = {"Authorization": f"Bearer {self._access_token}"}
        Utils.debug(f"Request headers are: {headers}")
        return headers

    def search_food(self, query: str):
        """Method to search for food items using FatSecret's search API."""
        headers = self._get_auth_headers()
        method: MethodParam = "foods.search.v3"
        # server.api?search_expression=Albume d'uovo conad&method=foods.search.v3&format=json
        params: RequestParams = {
            "search_expression": query,
            "method": method,
            "format": "json",
        }
        try:
            Utils.debug(f"search food by: {query}")
            response = Request().get(
                endpoint="server.api", params=params, headers=headers
            )
            return response.json()

        except exceptions.HTTPError as e:
            # If an HTTP error is raised, include the details in the exception
            error_detail = f"Failed to search food. Status Code: {e.response.status_code}, Response: {e.response.text}"
            raise ValueError(error_detail) from e


if __name__ == "__main__":
    query = input("Enter food name for test")
    instance = FatSecretController()
    response = instance.search_food(query=query)
    Utils.debug("Response\n", response)
