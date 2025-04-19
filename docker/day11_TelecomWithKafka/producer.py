from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'telecom-events'

def generate_event():
    return {
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "imsi": f"46001{random.randint(100000000, 999999999)}",
        "event": random.choice(["UL_Throughput_Low", "Reestablishment", "Attach_Request", "Detach_Request"]),
        "band": random.choice(["B5", "B3", "B40"]),
        "bw": random.choice(["5MHz", "10MHz", "20MHz"]),
        "ue_id": random.randint(1000, 2000)
    }

for _ in range(10):
    event = generate_event()
    producer.send(topic, event)
    print(f"[Producer] Sent: {event}")
    time.sleep(1)

producer.flush()

