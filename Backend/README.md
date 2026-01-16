# 🌍 AI Current Affairs Backend (FastAPI + CrewAI + Groq + Pinecone + Firecrawl)

This backend fetches live news from the web, summarizes it using LLM agents,  
and stores summaries in Pinecone for history and retrieval.

---

## 🚀 Tech Stack
- **FastAPI** – API framework  
- **CrewAI** – Multi-agent workflow  
- **Groq** – Fast and cheap Llama 3.1 inference  
- **Firecrawl** – Web scraping/search  
- **Pinecone** – Vector storage for summaries  
- **Uvicorn** – ASGI server  
- **Python 3.11**

---

## 📁 Project Structure

backend/
│── app/
│ ├── main.py ▶ FastAPI endpoints
│ ├── agents.py ▶ CrewAI agents (researcher + summarizer)
│ ├── tasks.py ▶ Tasks for agents
│ ├── crew_runner.py ▶ Runs agent workflow
│ ├── db.py ▶ Pinecone upsert & fetch
│
├── requirements.txt
├── .env ▶ API keys (DO NOT COMMIT)
└── README.md


---

## 🔑 Environment Variables

Create a `.env` file:

GROQ_API_KEY=your_groq_key
FIRECRAWL_API_KEY=your_firecrawl_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX=current-news


---

## 📦 Install Dependencies

Create virtual environment:

```bash
python -m venv news
news\Scripts\activate
pip install -r requirements.txt

▶️ Run Server
uvicorn app.main:app --reload

API now running at:
http://127.0.0.1:8000

Docs available at:
http://127.0.0.1:8000/docs

