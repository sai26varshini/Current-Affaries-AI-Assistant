import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/current-affairs"
HISTORY_URL = "http://127.0.0.1:8000/news-history"

def get_news(query):
    try:
        res = requests.get(API_URL, params={"q": query})
        if res.status_code == 200:
            data = res.json()
            return f"📌 Source: {data.get('source')}\n\n📰 {data.get('news')}"
        else:
            return "❌ Server error: " + str(res.text)
    except Exception as e:
        return f"⚠️ Request failed: {e}"

title = "🌍 AI Current Affairs News Dashboard"
description = """
Type any topic (example: **today india news**, **world tech news**, **sports update**)  
and get summarized headlines fetched from live internet sources 🚀
"""

ui = gr.Interface(
    fn=get_news,
    inputs=gr.Textbox(label="Enter topic", placeholder="today world news"),
    outputs=gr.Textbox(label="AI Summary", lines=15),
    title=title,
    description=description,
    theme="freddyaboulton/dracula_revamped"  # nice dark theme
)

ui.launch()
