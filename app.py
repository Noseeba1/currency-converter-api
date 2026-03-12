from fastapi import FastAPI
from routes import currency_routes
import os

app = FastAPI(
    title="Currency Converter API",
    description="RESTful API For Currency Converter",
    version="1.0.0"
)

PORT = int(os.getenv("PORT", 8000))

RATE_FILE = os.getenv("RATE_FILE", "data/rates.json")

# Logging Routes
app.include_router(currency_routes.router)

#  Checking Server
@app.get("/", status_code=200)
def checking_server():
    return {"message": "Currency Converter API is running"}
def read_root():
    return {"message": f"Server running on port {PORT}, using rates from {RATE_FILE}"}