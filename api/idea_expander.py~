from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your Streamlit app URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IdeaRequest(BaseModel):
    idea: str

@app.post("/expand-idea")
def expand_idea(request: IdeaRequest):
    # Use DeepSeek-V3 to expand the idea
    prompt = f"Expand this idea into a detailed book outline: {request.idea}"
    try:
        response = requests.post(
            "https://api.deepseek.com/chat/completions",  # Correct DeepSeek API endpoint
            headers={"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"},
            json={
                "model": "deepseek-chat",  # Use DeepSeek-V3
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                "stream": False  # Set to True for streaming responses
            }
        )
        response.raise_for_status()  # Raise an error for bad status codes
        return {"outline": response.json()["choices"][0]["message"]["content"]}
    except requests.exceptions.RequestException as e:
        return {"outline": {"error_msg": str(e)}}
