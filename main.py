import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()
# Get AI proxy token from environment variables
AI_PROXY_TOKEN = os.getenv("AI_PROXY_TOKEN")

if not AI_PROXY_TOKEN:
    raise ValueError("AI_PROXY_TOKEN is not set. Please configure it in Vercel.")


# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from JSON file
MARKS_FILE = Path("q-vercel-python.json")


def load_marks():
    if MARKS_FILE.exists():
        with open(MARKS_FILE, "r") as file:
            return json.load(file)
    return {}

marks_data = load_marks()

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    marks = [marks_data.get(n, 0) for n in name]  # Default to 0 if name not found
    return {"marks": marks, "ai_proxy_token": AI_PROXY_TOKEN}  # Debugging token}

