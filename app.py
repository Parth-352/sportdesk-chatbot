import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from engine.nlp import engine
from engine.event_db import (
    init_db,
    get_fixtures,
    get_active_delays,
    set_delay,
    get_facilities
)

app = FastAPI(title="SportDesk - Sports Event Management Assistant", version="1.0.0")

# Initialize SQLite database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Serve static directory
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def get_root():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "SportDesk API is active. Open /docs for API documentation."}

class ChatRequest(BaseModel):
    message: str

class DelayRequest(BaseModel):
    location: str
    delay_minutes: int
    message: str

@app.post("/api/chat")
def handle_chat(req: ChatRequest):
    query = req.message.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Empty query string")
    
    result = engine.predict(query)
    return result

@app.get("/api/fixtures")
def list_fixtures(sport: Optional[str] = None):
    return {"fixtures": get_fixtures(sport)}

@app.get("/api/delays")
def list_delays():
    return {"delays": get_active_delays()}

@app.post("/api/delays")
def report_delay(req: DelayRequest):
    set_delay(req.location, req.delay_minutes, req.message, is_active=True)
    return {"status": "success", "message": f"Delay registered for {req.location}"}

@app.get("/api/facilities")
def list_facilities(query: Optional[str] = None):
    return {"facilities": get_facilities(query)}

@app.get("/api/status")
def system_status():
    return {
        "status": "healthy",
        "engine": "NLTK + TF-IDF Cosine Similarity",
        "database": "SQLite (Live Fixtures & Delays)",
        "cached_patterns": len(engine.corpus_patterns)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
