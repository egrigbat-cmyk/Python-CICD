from fastapi import FastAPI

app = FastAPI(title="Deploymnent Health API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/version")
def get_version():
    return {
        "application": "Deployment Health API",
        "version": "1.0.0"
    }
