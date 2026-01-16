from crewai import Agent, LLM
from crewai_tools import FirecrawlSearchTool
import os

firecrawl_key = os.getenv("FIRECRAWL_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")

search_tool = FirecrawlSearchTool(api_key=firecrawl_key, max_results=5)

def get_researcher():
    return Agent(
        role="News Researcher",
        goal="Search internet & collect today's latest verified news",
        backstory="Expert real-time journalist scanning live sources",
        tools=[search_tool],
        verbose=True,   
        llm=LLM(
            model="llama-3.1-8b-instant",
            api_key=groq_key
        ),
        allow_delegation=False
    )

def get_summarizer():
    return Agent(
        role="News Summarizer",
        goal="Convert collected stories into 5 bullet points",
        backstory="Professional analyst who simplifies info",
        verbose=True,
        llm=LLM(
            model="llama-3.1-8b-instant",
            api_key=groq_key
        ),
    )
