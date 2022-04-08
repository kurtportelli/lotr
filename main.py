import os
import requests
from fastapi import FastAPI

app = FastAPI()

source_api_base_path = os.getenv("SOURCE_API_BASE_PATH")


@app.get("/all_books")
def fetch_books():
    url = os.path.join(source_api_base_path, "book")
    response = requests.get(url)
    return response.json()