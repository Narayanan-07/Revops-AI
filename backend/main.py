from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import form, webhooks, transcript
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="RevOps AI - Backend")

# Allow the Vite frontend to call the API (lead form + transcript upload).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form.router)
app.include_router(webhooks.router)
app.include_router(transcript.router)

@app.get("/")
def read_root():
    return {"message": "RevOps AI Backend Running"}
