from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (You can restrict this to your Weebly URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to your website URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Stock Screener API is running!"}
