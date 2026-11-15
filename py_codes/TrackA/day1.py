# Python + FastAPI: Hello Backend
# pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

# First route - this IS the backend
@app.get("/")
def home():
    # Equivalent to res.send()
    return "Hello from Python Backend! 👋"

@app.get("/api/user")
def get_user():
    # FastAPI auto-converts dict to JSON
    return {
        "id": 1,
        "name": "Abass",
        "role": "backend dev"
    }

# Run: uvicorn main:app --reload
# Visit http://localhost:8000