from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow Weebly frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to your website URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Replace this with a real API (We are using a free stock API for now)
STOCK_API_URL = "https://api.polygon.io/v2/aggs/ticker/NSE:INFY/prev?apiKey=YOUR_API_KEY"

@app.get("/")
def home():
    return {"message": "Stock Screener API is running!"}

@app.get("/stocks")
def get_stocks(pe_ratio: float = Query(None), market_cap: float = Query(None), volume: float = Query(None)):
    """ Fetch real stock data and filter based on parameters """
    
    # Get real-time stock data (replace with NSE/BSE API)
    response = requests.get(STOCK_API_URL)
    data = response.json()
    
    # Simulated stock data (Replace with real stock data)
    stocks = [
        {"symbol": "INFY", "pe_ratio": 28.5, "market_cap": 100000, "volume": 50000},
        {"symbol": "TCS", "pe_ratio": 30.2, "market_cap": 150000, "volume": 80000},
        {"symbol": "RELIANCE", "pe_ratio": 25.8, "market_cap": 200000, "volume": 100000}
    ]

    # Apply filters
    if pe_ratio:
        stocks = [s for s in stocks if s["pe_ratio"] <= pe_ratio]
    if market_cap:
        stocks = [s for s in stocks if s["market_cap"] >= market_cap]
    if volume:
        stocks = [s for s in stocks if s["volume"] >= volume]

    return {"stocks": stocks}
