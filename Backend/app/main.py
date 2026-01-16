from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query
from app.db import save_news, get_news
from app.crew_runner import run_news

app = FastAPI()

@app.get("/news-history")
def read_history(limit: int = 5):
    return get_news(limit)

@app.get("/current-affairs")
def fetch_news(q: str = "today news"):
    # First, check cache
    cached = get_news()
    if cached:
        return {"source": "pinecone", "news": cached}

    # Run agents if not cached
    summary = run_news(q)
    save_news(summary)
    return {"source": "crew", "news": summary}
