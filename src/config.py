import os

BASE_URL = "https://platform.fatsecret.com/rest"
API_CLIENT_ID = os.getenv("API_CLIENT_ID")  # Reads from environment variable
API_CLIENT_SECRET = os.getenv("API_CLIENT_SECRET")  # Reads from environment variable

if not API_CLIENT_ID or not API_CLIENT_SECRET:
    raise ValueError(
        "API_CLIENT_ID and API_CLIENT_SECRET must be set as environment variables."
    )
