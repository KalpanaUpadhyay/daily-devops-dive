Kafka Basics (10 min)

Apache Kafka is a distributed event streaming platform:

Producer: Sends messages to topics

Consumer: Reads messages from topics

Broker: Kafka server that handles messages

Zookeeper: Manages Kafka cluster metadata (still required in many Kafka setups)

Kafka is great for real-time data pipelines, logs, and telecom event flows.


Produce and Consume a Message (10 min)

Enter the Kafka container:
docker exec -it <container_id_of_kafka> bash
Now produce a message:

# Create a topic
kafka-topics --bootstrap-server localhost:9092 --create --topic test-topic --partitions 1 --replication-factor 1

# Produce
kafka-console-producer --broker-list localhost:9092 --topic test-topic
> Hello Kafka!
In another terminal (or another Kafka shell):
# Consume
kafka-console-consumer --bootstrap-server localhost:9092 --topic test-topic --from-beginning
You should see your message (Hello Kafka!) pop up!
