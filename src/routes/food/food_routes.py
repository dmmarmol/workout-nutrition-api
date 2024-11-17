# src/routes/fatsecret_routes.py
from fastapi import APIRouter

# from controllers.food_diary_controller import FoodDiaryController
from controllers.fatsecret_controller import FatSecretController

food_router = APIRouter()

# food_controller = FoodDiaryController()

# @food_diary_router.get("/entries/{date}")
# async def get_entries(date: str):
#     return food_controller.get_entries(date)

# =================================
# Nutrition Api Routes are defined below
# =================================
fatsecret_controller = FatSecretController()


@food_router.get("/search/{search_term}")
async def search_food(search_term: str):
    return fatsecret_controller.search_food(search_term)
