from flask import Flask
import os

app = Flask(__name__)
counter_file = "/data/counter.txt"

@app.route('/')
def home():
    if not os.path.exists(counter_file):
        with open(counter_file, 'w') as f:
            f.write("0")

    with open(counter_file, 'r+') as f:
        count = int(f.read()) + 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return f"Hello Kalpana! File-based counter: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

