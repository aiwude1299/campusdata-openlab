from fastapi import FastAPI

app = FastAPI(title="CampusData-OpenLab API", version="0.1.0")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "CampusData-OpenLab Academic API",
        "version": "0.1.0",
        "environment": "Education / Research Sandbox"
    }

@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy", "database": "connected"}
