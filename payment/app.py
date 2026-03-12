from flask import Flask
import requests
import time

app = Flask(__name__)

@app.route("/process")
def payment():

    # simulate processing time (μ = 60 req/s)
    time.sleep(1/60)

    response = requests.get("http://database:5002/query")

    return "Payment Service → " + response.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)