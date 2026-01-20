from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = Path(__file__).parent / "data"

def load_items():
    items = []
    for file in DATA_DIR.glob("*.json"):
        with open(file) as f:
            items.extend(json.load(f))
    return items

@app.get("/items")
def get_items(color: str | None = None):
    items = load_items()
    if color:
        items = [i for i in items if i["color"] == color]
    return items
