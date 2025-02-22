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

class WriteRequest(BaseModel):
    outline: str
    research: str

@app.post("/write-chapter")
def write_chapter(request: WriteRequest):
    prompt = f"Write a chapter based on this outline: {request.outline}. Use this research: {request.research}."
    response = requests.post(
        "https://api.deepseek.com/v3/generate",
        headers={"Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"},
        json={"prompt": prompt, "max_tokens": 2000}
    )
    return {"chapter": response.json()}
