✅ Day 16: Cassandra Basics — CQL + Data Modeling
🧠 What You’ll Learn:
Use CQL (Cassandra Query Language) from inside the pod

Create a keyspace, table, insert and query data

🛠️ Steps:
1. Enter the Cassandra Pod
kubectl exec -it cassandra-0 -- cqlsh

2. Create a Keyspace
CREATE KEYSPACE kalpana_space WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

3. Use the Keyspace
USE kalpana_space;

4. Create a Table
CREATE TABLE users (
  id UUID PRIMARY KEY,
  name TEXT,
  email TEXT
);

5. Insert Some Data

INSERT INTO users (id, name, email)
VALUES (uuid(), 'Kalpana', 'kalpana@example.com');
Insert a few more if you want, just with different names.

6. Query the Table

SELECT * FROM users;
You’ll see something like:

id                                   | name     | email
------------------------------------+----------+-----------------------
5e4b050e-1a57-45e6-8149-bf1f27...   | Kalpana  | kalpana@example.com

7. Exit CQL
exit;


💡 Tips:
Cassandra is NoSQL, but structured.

Think of tables as pre-modeled for how you want to query, not normalized like in SQL.

Keep your queries simple — no JOINs, no GROUP BYs.
