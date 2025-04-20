Day 12 is going to be extra exciting — we’ll connect all the dots and build a small end-to-end logging pipeline using modern tools.

Day 12: Kafka → FastAPI REST → MongoDB


🧱 Stack We’re Using:
Kafka: Event ingestion (already running)

FastAPI: REST API for monitoring/querying events

MongoDB: To store all events (replaceable with Cassandra later)

 Run Everything
Start your FastAPI app:

uvicorn main:app --reload
Then hit:

http://localhost:8000/

http://localhost:8000/events

http://localhost:8000/events/by_band/B5

Your FastAPI is now showing real Kafka telecom events pulled into MongoDB!
