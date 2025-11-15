# 🤖 Enterprise Policy Assistant

Domain-aware RAG chatbot with **Groq API + FastAPI + Streamlit**

## 📂 Project Structure

```
domain_aware_chat/
├── data/
│   └── enterprise_policies.txt
├── modules/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── embed_store.py
│   ├── retriever.py
│   └── chat_engine.py
├── backend.py
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

## 🔧 Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get API Keys

**Groq API Key** (for LLM inference):
1. Visit https://console.groq.com/keys
2. Create a new API key

**Google API Key** (for Gemini embeddings):
1. Visit https://makersuite.google.com/app/apikey
2. Create a new API key

Add both to `.env`:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Create modules/__init__.py

```bash
touch modules/__init__.py
```

### 4. Add Your Data

Place your policy documents in `data/enterprise_policies.txt`

## 🚀 Run the Application

### Terminal 1: Start FastAPI Backend

```bash
uvicorn backend:app --reload
```

Backend runs on: **http://localhost:8000**

### Terminal 2: Start Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Frontend opens at: **http://localhost:8501**

## 💬 Usage

1. Open Streamlit UI in browser
2. Ask questions like:
   - "What's the remote work policy?"
   - "How many leave days do I get?"
   - "What's the expense reimbursement policy?"
3. View answers with source citations

## 🔄 Rebuild Index

Click "🔄 Rebuild Index" in sidebar to reprocess documents after updates.

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Groq API (Llama 3.3 70B) |
| Embeddings | SentenceTransformers |
| Vector Store | FAISS |
| Framework | LangChain |
| Backend | FastAPI |
| Frontend | Streamlit |

## 📊 API Endpoints

- `GET /` - Health check
- `POST /query` - Ask questions
- `POST /rebuild-index` - Rebuild vector store

## 🎯 Features

- ✅ Fast inference with Groq
- ✅ Local embeddings (free)
- ✅ Source citations
- ✅ Chat history
- ✅ Easy to extend with more documents
- ✅ Modern UI with Streamlit
- ✅ RESTful API with FastAPI

## 🔜 Next Steps

- Add multi-document support
- Implement authentication
- Add conversation memory
- Deploy to production
- Add document upload feature

## 📦 Deploying Backend to Vercel (Serverless)

You can deploy the backend to Vercel as a serverless Python app. This approach is only recommended if the backend does NOT rely on heavy native dependencies that fail to build (FAISS tends to fail in serverless environments). If your app requires FAISS, use Render/Heroku/Azure instead.

Steps:

1. Vercel config is already included: `api/index.py` re-exports the `FastAPI` `app` from `backend.py` and `vercel.json` configures the Python build.
2. Add environment variables on Vercel project (Settings → Environment Variables) for any secrets such as `GROQ_API_KEY`.
3. Remove `faiss-cpu` from the Vercel `requirements.txt` if your build fails, or switch to a hosted vector DB.
4. Install and log in with Vercel CLI and deploy:

```bash
npm i -g vercel
vercel login
vercel --prod
```

Notes & Caveats:
- `faiss-cpu` is a native dependency and often fails to build in Vercel serverless. Consider replacing with Pinecone/Weaviate or prebuild the `faiss_index` and store it in S3.
- `.vercelignore` is already included to avoid pushing `faiss_index/` and `data/` (sensitive or large files) to Vercel.

If you prefer not to use Vercel for the backend, see the `Render` or `Heroku` sections earlier in this README.