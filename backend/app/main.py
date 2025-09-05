from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "OffSec SaaS API is running 🚀"}