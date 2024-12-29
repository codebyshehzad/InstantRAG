from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self):
        # Load an open-source embedding model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    async def get_embeddings(self, text: str) -> list:
        try:
            # Generate embeddings using Sentence Transformers
            embedding = self.model.encode(text)
            return embedding.tolist()
        except Exception as e:
            raise Exception(f"Error generating embeddings: {str(e)}")

