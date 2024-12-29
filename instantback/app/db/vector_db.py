# File: app/db/vector_db.py
from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings

def get_vector_db():
    # Create an instance of Pinecone
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)

    # Check if the specified index exists
    if settings.PINECONE_INDEX_NAME not in pc.list_indexes().names():
        # Create the index if it doesn't exist
        pc.create_index(
            name=settings.PINECONE_INDEX_NAME,
            dimension=settings.VECTOR_DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",  # Use the correct cloud provider
                region="us-east-1"  # Your specified region
            )
        )

    # Get the specified index
    return pc.Index(settings.PINECONE_INDEX_NAME)