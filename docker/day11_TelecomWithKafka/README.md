Day 11: Simulate Telecom Events → Push to Kafka via Python

Goal:Simulate a realistic IMSI catcher/UL throughput/log message in Python, push it to Kafka, and consume it in real time.

✅ What You’ll Build Today:
A dummy event generator (like what your OAI/agent might produce)

A Kafka producer that pushes these events

A Kafka consumer that could simulate a backend log or dashboard listener


Run It!
Start your Kafka stack:

docker-compose up -d

Open two terminals:

Terminal 1:

python3 consumer.py 

Terminal 2:

python3 producer.py


You’ll see real-time telecom-like events flowing between producer and consumer — just like how your OAI agent might push logs or alarms to a backend.


