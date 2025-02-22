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
    # Use OpenAI GPT to expand the idea
    prompt = f"Expand this idea into a detailed book outline: {request.idea}"
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
                "max_tokens": 1000
            }
        )
        response.raise_for_status()  # Raise an error for bad status codes
        return {"outline": response.json()["choices"][0]["message"]["content"]}
    except requests.exceptions.RequestException as e:
        return {"outline": {"error_msg": str(e)}}
