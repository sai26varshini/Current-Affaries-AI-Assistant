import asyncio
import datetime
from app.crew_runner import run_news
from app.db import save_news

REFRESH_HOURS = 4
last_run = None

async def refresh_loop():
    global last_run
    while True:
        now = datetime.datetime.utcnow()
        if last_run is None or (now - last_run).total_seconds() > REFRESH_HOURS * 3600:
            try:
                summary = run_news()
                save_news(summary)
                last_run = now
                print("Auto-refreshed news summary")
            except Exception as e:
                print(f"Refresh failed: {e}")
        await asyncio.sleep(60)
