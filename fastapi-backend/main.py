from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="My FastAPI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!", "status": "running"}

@app.get("/api/items")
def get_items():
    return [
        {"id": 1, "name": "FastAPI Item 1", "price": 10.99},
        {"id": 2, "name": "FastAPI Item 2", "price": 20.99},
    ]

@app.post("/api/items")
def create_item(item: Item):
    return {"message": "Item created", "item": item}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "backend": "FastAPI"}