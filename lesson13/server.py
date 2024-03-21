import time
import httpx
import random
import string
from typing import Callable

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

cached_data = ""
last_request_time = 0

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


@app.post("/fetch-market")\

def get_current_market_state(payload: dict):
    global cached_data, last_request_time
    source = payload.get("source")
    destination = payload.get("destination")

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={destination}&apikey=demo"
        # responce = requests.get(url) 


    current_time = time.time()
    if current_time - last_request_time >= 10:
        response = requests.get(url)
        data = response.json()
        rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        current_time = time.time()
        cached_data = rate
        last_request_time = current_time
        return {cached_data}
    else:
        return {cached_data}

        

        #http://localhost:8000/fetch-market?source=EUR&destination=USD
        #http://localhost:8000/fetch-market 
    
    # """Response example:
    #    {
    #     "Realtime Currency Exchange Rate": {
    #         "1. From_Currency Code": "UAH",
    #         "2. From_Currency Name": "Ukrainian Hryvnia",
    #         "3. To_Currency Code": "USD",
    #         "4. To_Currency Name": "United States Dollar",
    #         "5. Exchange Rate": "0.02610000",
    #         "6. Last Refreshed": "2024-03-07 17:45:47",
    #         "7. Time Zone": "UTC",
    #         "8. Bid Price": "0.02609000",
    #         "9. Ask Price": "0.02610000"
    #     }
    # }
    # """