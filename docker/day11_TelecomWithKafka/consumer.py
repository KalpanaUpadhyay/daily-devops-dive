from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'telecom-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='monitoring-service',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("[Consumer] Waiting for events...\n")
for message in consumer:
    print(f"[Consumer] Received: {message.value}")

