#FastAPI Server

from fastapi import FastAPI
from pymongo import MongoClient
from kafka_consumer import start_consumer_thread

app = FastAPI()
start_consumer_thread()

client = MongoClient("mongodb://localhost:27017/")
db = client["telecom"]
events_col = db["events"]

@app.get("/")
def read_root():
    return {"msg": "Kafka + FastAPI + MongoDB is alive!"}

@app.get("/events")
def get_all_events():
    events = list(events_col.find({}, {"_id": 0}))
    return {"events": events}

@app.get("/events/by_band/{band}")
def get_events_by_band(band: str):
    events = list(events_col.find({"band": band}, {"_id": 0}))
    return {"events": events}

