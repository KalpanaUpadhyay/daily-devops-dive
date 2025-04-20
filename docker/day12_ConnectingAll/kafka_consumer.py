from kafka import KafkaConsumer
import json
from pymongo import MongoClient
import threading

def consume_kafka():
    consumer = KafkaConsumer(
        'telecom-events',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='api-logger',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    client = MongoClient("mongodb://localhost:27017/")
    db = client["telecom"]
    events_col = db["events"]

    print("[KafkaConsumer] Listening for events...")
    for msg in consumer:
        event = msg.value
        print(f"[KafkaConsumer] Storing: {event}")
        events_col.insert_one(event)

def start_consumer_thread():
    thread = threading.Thread(target=consume_kafka)
    thread.daemon = True
    thread.start()

