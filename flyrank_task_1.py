from fastapi import FastAPI

# Create the FastAPI application (our backend server)
app = FastAPI()


# -------------------- Endpoint 1 --------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to my first backend!",
        "status": "Server is running successfully"
    }


# -------------------- Endpoint 2 --------------------

@app.get("/student")
def student():
    return {
        "name": "Muhammad Ahmad",
        "university": "COMSATS University Islamabad",
        "program": "BS Electronics and Computing",
        "semester": 4
    }