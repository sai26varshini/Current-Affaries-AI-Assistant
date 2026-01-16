from crewai import Crew
from app.agents import get_researcher, get_summarizer
from app.tasks import create_tasks
from groq import Groq
import os


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_news(query="latest breaking world news today"):
    r = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"user",
                "content":f"Give 3 bullet trending news on: {query}. Max 80 words."
            }
        ]
    )
    return r.choices[0].message.content