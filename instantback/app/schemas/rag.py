# File: schemas/rag.py
from pydantic import BaseModel
from typing import Optional, List

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

class DocumentResponse(BaseModel):
    status: str
    filename: str
    doc_id: str
