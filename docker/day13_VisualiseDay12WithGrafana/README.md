 Day 13: Visualize Kafka Events in Grafana (via MongoDB as datasource)

🎯 Goal: Connect Grafana to MongoDB → Display dashboards of telecom events

Update your docker-compose.yml(Copy from day 12 and add grafana image)

Then start it up: docker compose up -d

Visit: http://localhost:3000
Login with default: admin / admin → Set a new password

🔌 Step 2: Add MongoDB Plugin to Grafana
Grafana doesn’t ship with MongoDB plugin by default.

You can install it by running this (one-time):

docker exec -it grafana grafana-cli plugins install marcusolsson-mongodb-datasource
docker restart grafana

Note: If that fails, we can use Grafana with MongoDB plugin pre-bundled, or you can build a custom Docker image — I’ll guide you if needed.

🧷 Step 3: Connect MongoDB in Grafana
Go to Grafana → Settings → Data Sources → Add data source

Choose MongoDB (if the plugin is installed)

Set:

URL: mongodb://mongodb:27017

Database: telecom

Collection: events

Save & Test ✅

📊 Step 4: Create Dashboard
Now create a dashboard to visualize Kafka events:

Dashboard → New Panel

Query (MongoDB):

json


{
  "find": "events",
  "filter": {},
  "projection": { "band": 1, "event": 1, "_id": 0 },
  "limit": 100
}

Visualization: choose Table or Bar Chart

You can also use:

Group by "band" → Count

Show how many events came per band (B5, B40, etc.)

Create time-series using timestamps (if you include those in Day 11’s producer)



#P.S: You may get enterprise issue for mongo DB, you can change it to free/trial version
