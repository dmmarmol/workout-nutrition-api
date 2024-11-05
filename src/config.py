import os

BASE_URL = "https://platform.fatsecret.com/rest/server.api"
CLIENT_ID = os.getenv("CLIENT_ID")  # Reads from environment variable
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # Reads from environment variable

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError(
        "CLIENT_ID and CLIENT_SECRET must be set as environment variables."
    )
