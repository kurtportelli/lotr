import os
import requests
from fastapi import FastAPI

app = FastAPI()

source_api_base_path = os.getenv("SOURCE_API_BASE_PATH")
access_token = os.getenv("ACCESS_TOKEN")


def fetch_items(item):
    url = os.path.join(source_api_base_path, item, "?limit=10000")
    response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
    return response.json()

@app.get("/fetch_data")
def fetch_data_from_source_api():
    items = ["book", "movie", "character", "quote", "chapter"]
    return {f"{item}s_data": fetch_items(item) for item in items}
