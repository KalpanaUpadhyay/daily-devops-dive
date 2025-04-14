# Day 6: Docker + Flask + PostgreSQL 🔥

This mini project demonstrates how to run a Flask web app with a PostgreSQL database using Docker Compose.

Every time you refresh the page, a visit is recorded in the PostgreSQL database!

---

## 🧱 Stack

- Python 3.9
- Flask
- PostgreSQL 13
- Docker & Docker Compose

---

## 🚀 How to Run

### 1. Clone this repo

```bash
git clone https://github.com/kalpana-devops/docker-learning-series.git
cd docker-learning-series/day6-postgres


day6-postgres/
├── app/
│   ├── app.py              # Flask app using SQLAlchemy
│   └── requirements.txt    # Flask + PostgreSQL dependencies
├── Dockerfile              # Flask image build
├── docker-compose.yml      # Compose to run Flask + PostgreSQL
└── README.md

PostgreSQL container runs with:

User: kalpana

Password: pass

Database: kalpana_db

DB data is persisted using a Docker volume (pgdata).

🧼 Clean Up
To stop and remove everything:


sudo docker compose down
To also delete the data volume:

sudo docker compose down -v
