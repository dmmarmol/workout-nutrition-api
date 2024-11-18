from config import API_ENV


class Utils:
    def __init__(self):
        pass

    def debug(message: str):
        if API_ENV == "development":
            print(f"[DEBUG] {message}")
