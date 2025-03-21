import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from JSON file
MARKS_FILE = Path("C:\Users\hp\my-api-project\q-vercel-python.json")

def load_marks():
    if MARKS_FILE.exists():
        with open(MARKS_FILE, "r") as file:
            return json.load(file)
    return {}

marks_data = load_marks()

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    marks = [marks_data.get(n, 0) for n in name]  # Default to 0 if name not found
    return {"marks": marks}

