# File: routers/items.py
from fastapi import APIRouter, Depends
from app.routers.auth import oauth2_scheme

router = APIRouter()

@router.get("/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"items": []}