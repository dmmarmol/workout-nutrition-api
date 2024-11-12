from fastapi import FastAPI
from routes.food import food_diary_route
import uvicorn

app = FastAPI()

# Include the routes from the api module
app.include_router(food_diary_route.food_diary_router, prefix="/api")

if __name__ == "__main__":

    print("Welcome to the Nutrition API")
    print("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
