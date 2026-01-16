from groq import Groq
from pinecone import Pinecone
import uuid
import os

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX"))

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

EMBED_MODEL = "text-embedding-3-small"  # <-- Correct & available

def embed(text: str):
    res = groq_client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return res.data[0].embedding

def save_news(text: str):
    try:
        vector = embed(text)

        index.upsert([
            {
                "id": str(uuid.uuid4()),
                "values": vector,
                "metadata": {"summary": text[:500]}
            }
        ])
        print("Saved to Pinecone!")
    except Exception as e:
        print("Save failed:", e)

def get_news(limit: int = 5):
    try:
        # dimension of text-embedding-3-small is 1536
        dummy_vec = [0.0] * 1536
        res = index.query(
            vector=dummy_vec,
            top_k=limit,
            include_metadata=True
        )
        return [m.metadata.get("summary") for m in res.matches if m.metadata]
    except Exception as e:
        print("Fetch failed:", e)
        return []

