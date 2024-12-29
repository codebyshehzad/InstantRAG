# File: app/services/gemini_api.py
import google.generativeai as genai
from app.core.config import settings
import logging

class GeminiService:
    def __init__(self):
        self.logger = logging.getLogger("GeminiService")
        logging.basicConfig(level=logging.INFO)
        
        # Configure the Gemini API with your API key
        genai.configure(api_key=settings.GEMINI_API_KEY)
        
        # Get the model
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    async def generate_response(self, prompt: str) -> str:
        try:
            self.logger.info("Sending request to Gemini API...")
            self.logger.info(f"Prompt: {prompt}")
            
            # Generate content using the model
            response = self.model.generate_content(prompt)
            
            self.logger.info("Response received successfully")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Exception occurred: {e}")
            raise Exception(f"Error generating response with Gemini: {str(e)}")