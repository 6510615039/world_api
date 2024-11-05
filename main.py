import csv
from fastapi import FastAPI
from utils import get_data_from_csv

data_country = get_data_from_csv("world_table_country.csv")
data_city = get_data_from_csv("world_table_city.csv")

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello there"}

@app.get("/world")
async def read_countries() -> dict:
    return {"result": data_country}

@app.get("/world/country/{name}")
async def read_country(name: str) -> dict:
    for row in data_country:
        if row["Name"].lower() == name.lower():
            return {"result": row}
    return {"result": {}}

@app.get("/world/city/{name}")
async def read_city(name: str) -> dict:
    for row in data_city:
        if row["Name"].lower() == name.lower():
            return {"result": row}
    return {"result": {}}
