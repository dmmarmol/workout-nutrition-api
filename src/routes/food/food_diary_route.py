# src/routes/fatsecret_routes.py
from fastapi import APIRouter
from controllers.food_diary_controller import FoodDiaryController

food_diary_router = APIRouter()
food_controller = FoodDiaryController()


@food_diary_router.get("/entries/{date}")
async def get_entries(date: str):
    return food_controller.get_entries(date)
