# File: routers/rag.py
from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.langchain_rag import RAGService
from app.schemas.rag import QueryRequest, QueryResponse
from typing import List
import json

router = APIRouter()
rag_service = RAGService()

@router.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:
        response = await rag_service.process_query(request.query)
        return QueryResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        result = await rag_service.process_document(file)
        return {"message": "Document processed successfully", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 