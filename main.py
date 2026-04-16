from fastapi import FastAPI
from router import router

app = FastAPI(title="Book CRUD API", description="API com FastAPI + MongoDB + Docker")
app.include_router(router)

@app.get("/")
def home():
    return {"message": "📚 Book CRUD API - FastAPI + MongoDB + Docker"}