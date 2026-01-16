
---

# 🟦 **FRONTEND README.md (Gradio Dashboard)**

```markdown
# 📰 AI Current Affairs Frontend (Gradio Dashboard)

Frontend UI that allows users to request latest news
and view summarized output coming from the backend API.

---

## 🎯 Features
- Clean professional Gradio UI  
- Dark/Light theme support  
- Calls backend REST API  
- Displays structured summary  
- Works on HuggingFace Spaces or local machine

---

## 📁 Project Structure

frontend/
├── gradio_app.py
├── requirements.txt
└── README.md


---

## 🔧 Install Dependencies

```bash
pip install gradio requests
(if running from main requirements.txt, skip this)

▶️ Run Frontend

Make sure backend is already running at:
http://127.0.0.1:8000

Then start Gradio:
python dashboard.py

UI loads at:
http://127.0.0.1:7860

🔗 Backend Connection

Frontend sends GET request:
requests.get("http://127.0.0.1:8000/current-affairs?q=topic")

If deploying on HuggingFace, replace with your Render backend URL:
https://yourapp.onrender.com/current-affairs

