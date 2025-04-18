from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'test-topic'

for i in range(5):
    message = f"Message {i}".encode('utf-8')
    producer.send(topic, message)
    print(f"Sent: {message}")

producer.flush()

