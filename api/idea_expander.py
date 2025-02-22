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
    prompt = f"Expand this idea into a detailed book outline: {request.idea}"
    response = requests.post(
        "https://api.deepseek.com/v3/generate",
        headers={"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"},
        json={"prompt": prompt, "max_tokens": 1000}
    )
    return {"outline": response.json()}
