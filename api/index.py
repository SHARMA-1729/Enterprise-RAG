"""Vercel serverless wrapper for FastAPI backend.

Vercel will use `api/index.py` as the serverless entrypoint. We simply
re-export `app` from `backend.py` (which already defines a FastAPI app).

Notes:
- `backend.py` must not run the local server when imported. It currently
  uses `if __name__ == "__main__": uvicorn.run(...)` which prevents it from
  starting at import time (good).
- Vercel's Python runtime will import this file; it expects an ASGI app
  object named `app` to serve.
"""

from backend import app  # backend.py exposes `app = FastAPI(...)`

# Re-export `app` so the Vercel runtime can find an ASGI callable named `app`
__all__ = ["app"]
