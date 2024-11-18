import os

BASE_URL = "https://platform.fatsecret.com/rest"
API_ENV = os.getenv("API_ENV")
API_CLIENT_ID = os.getenv("API_CLIENT_ID")
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")

if not API_CLIENT_ID or not API_CLIENT_SECRET:
    raise ValueError(
        "API_CLIENT_ID and API_CLIENT_SECRET must be set as environment variables."
    )
