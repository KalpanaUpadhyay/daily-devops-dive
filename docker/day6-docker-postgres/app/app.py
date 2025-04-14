from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kalpana:pass@db:5432/kalpana_db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    visit = Visit()
    db.session.add(visit)
    db.session.commit()
    count = Visit.query.count()
    return f"Hello Kalpana! DB visit count: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

