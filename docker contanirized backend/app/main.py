from fastapi import FastAPI
from app.routes.students import router as student_router
# Create the FastAPI application
app = FastAPI(
    title="FlyRank Task 2 API",
    description="A simple User Management Backend using FastAPI",
    version="1.0.0"
)
app.include_router(student_router)
# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to FlyRank Task 2 API!",
        "status": "Application is running successfully."
    }