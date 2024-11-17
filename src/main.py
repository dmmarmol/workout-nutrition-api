from fastapi import FastAPI
from routes.food import food_routes
import uvicorn

app = FastAPI()

# Include the routes from the api module
app.include_router(food_routes.food_router, prefix="/api")

if __name__ == "__main__":
    print("Welcome to the Nutrition API")
    print("[DEBUG] Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
