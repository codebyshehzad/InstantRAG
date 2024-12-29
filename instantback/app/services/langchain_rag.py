# File: app/services/langchain_rag.py
from app.services.embeddings import EmbeddingService
from app.db.vector_db import get_vector_db
from app.services.gemini_api import GeminiService
import hashlib
from fastapi import UploadFile

class RAGService:
    def __init__(self):
        self.vector_db = get_vector_db()
        self.embedding_service = EmbeddingService()
        self.gemini_service = GeminiService()

    async def process_document(self, file: UploadFile) -> dict:
        try:
            # Read and process the file content
            content = await file.read()
            text = content.decode("utf-8")

            # Generate document ID
            doc_id = hashlib.md5(text.encode()).hexdigest()

            # Generate embeddings
            vector = await self.embedding_service.get_embeddings(text)

            # Upsert into Pinecone
            self.vector_db.upsert(vectors=[{
                "id": f"doc_{doc_id}",
                "values": vector,
                "metadata": {"text": text, "filename": file.filename},
            }])

            return {"status": "processed", "filename": file.filename, "doc_id": f"doc_{doc_id}"}
        except Exception as e:
            raise Exception(f"Error processing document: {str(e)}")

    async def process_query(self, query: str) -> str:
        try:
            # Generate query embeddings
            vector_query = await self.embedding_service.get_embeddings(query)

            # Query the vector database
            query_response = self.vector_db.query(
                vector=vector_query,
                top_k=3,
                include_metadata=True
            )

            # Extract relevant documents
            matches = query_response.get("matches", [])
            if not matches:
                return "No relevant documents found."

            # Create a context from relevant documents
            context = "\n".join([match["metadata"]["text"] for match in matches])

            # Augment the query with context
            augmented_query = (
                f"Context:\n{context}\n\n"
                f"Question: {query}\n\n"
                "Provide a detailed and accurate response."
            )

            # Generate response using Gemini
            response = await self.gemini_service.generate_response(augmented_query)
            return response
        except Exception as e:
            raise Exception(f"Error processing query: {str(e)}")
