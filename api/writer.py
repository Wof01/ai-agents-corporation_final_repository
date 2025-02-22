from fastapi import APIRouter
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class WriteRequest(BaseModel):
    outline: str
    research: str

@router.post("/")
def write_chapter(request: WriteRequest):
    # Use OpenAI GPT to write a chapter
    prompt = f"Write a chapter based on this outline: {request.outline}. Use this research: {request.research}."
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",  # OpenAI API endpoint
            headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
            json={
                "model": "gpt-3.5-turbo",  # Use a free-tier model
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 2000
            }
        )
        response.raise_for_status()  # Raise an error for bad status codes
        return {"chapter": response.json()["choices"][0]["message"]["content"]}
    except requests.exceptions.RequestException as e:
        return {"chapter": {"error_msg": str(e)}}
