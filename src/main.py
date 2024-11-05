from fastapi import FastAPI
from routes import router

app = FastAPI()

# Include the routes from the api module
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    print("Welcome to the Nutrition API")

    uvicorn.run(app, host="0.0.0.0", port=8000)
