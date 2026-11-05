from fastapi import FastAPI

app = FastAPI(
    title = "Webhook Delivery System",
    description = "A backend service for reliable webhook delivery",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {"message" : "Webhook Delivery System"}

@app.get("/health")
def health_check():
    return {
        "status" : "healthy"
    }