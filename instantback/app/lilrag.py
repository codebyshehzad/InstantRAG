import requests
import asyncio

async def test_rag():
    base_url = "http://localhost:8000/api/rag"
    
    # Test document upload
    with open("sample.txt", "r") as f:
        files = {'file': ('sample.txt', f, 'text/plain')}
        upload_response = requests.post(f"{base_url}/upload", files=files)
        print("Upload Response:", upload_response.json())
    
    # Test query
    query_data = {'query': 'who is bilal'}
    query_response = requests.post(f"{base_url}/query", json=query_data)
    print("Query Response:", query_response.json())

if __name__ == "__main__":
    asyncio.run(test_rag())
