from flask import Flask
import time

app = Flask(__name__)

@app.route("/query")
def database():

    # simulate database processing (μ = 80 req/s)
    time.sleep(1/80)

    return "Database Response"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)