from fastapi import FastAPI
from routes import form, webhooks
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="ContextBridge - Person 1 Backend")

app.include_router(form.router)
app.include_router(webhooks.router)

@app.get("/")
def read_root():
    return {"message": "Person 1 Backend Running"}
