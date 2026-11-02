from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Docker Demo",
    description="My first application for learning deployment",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Hello! My FastAPI application is running.",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
