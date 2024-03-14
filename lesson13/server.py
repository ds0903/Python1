import httpx
import random
import string
from typing import Callable

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

create_random_string: Callable[[int], str] = lambda size: "".join(
    [random.choice(string.ascii_letters) for _ in range(size)]
)


@app.post("/generate-article")
async def get_information():
    """This endpoint returns the random information"""

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }


@app.post("/fetch-market")
def get_current_market_state(payload: dict):
    source = payload.get("source")
    destination = payload.get("destination")

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={destination}&apikey=V2V43QAQ8RILGBOW"
        # responce = requests.get(url) 
    response = requests.get(url)

    data = response.json()
    rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    
    return {"rate": rate}

        

        #http://localhost:8000/fetch-market?source=EUR&destination=USD
        #http://localhost:8000/fetch-market