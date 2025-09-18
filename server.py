import os
import csv
import json
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from groq import Groq

# Load .env file
load_dotenv()

# Get API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")  # put index.html inside /templates


def analyze_transcript(transcript: str):
    """
    Analyze transcript using Groq's Chat Completions API.
    Returns: (summary, sentiment, error)
    """
    if not GROQ_API_KEY:
        return None, None, "Error: GROQ_API_KEY not set."

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # ✅ recommended model
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that analyzes customer service calls."
                },
                {
                    "role": "user",
                    "content": f"""
                    Analyze the following customer call transcript and provide:
                    1. A concise summary (2-3 sentences)
                    2. The customer's sentiment (positive, neutral, or negative)

                    Transcript: {transcript}

                    Respond ONLY in strict JSON: {{"summary": "...", "sentiment": "..."}}
                    """
                }
            ],
            temperature=0.2,
            max_tokens=300,
        )

        # Extract assistant response
        content = completion.choices[0].message.content.strip()

        # Parse JSON response
        parsed = json.loads(content)
        return parsed.get("summary"), parsed.get("sentiment"), None

    except Exception as e:
        return None, None, f"API error: {str(e)}"


def save_to_csv(transcript, summary, sentiment):
    """
    Save transcript, summary, and sentiment to CSV.
    """
    file_exists = os.path.isfile("call_analysis.csv")
    with open("call_analysis.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Transcript", "Summary", "Sentiment"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "Transcript": transcript,
            "Summary": summary,
            "Sentiment": sentiment,
            
        })


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Serve the HTML frontend (index.html).
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze")
async def analyze(transcript: str = Form(...)):
    """
    API endpoint: analyze transcript → summary + sentiment.
    """
    summary, sentiment, error = analyze_transcript(transcript)
    if error:
        return JSONResponse({"error": error}, status_code=500)

    save_to_csv(transcript, summary, sentiment)
    return {"transcript": transcript, "summary": summary, "sentiment": sentiment}
