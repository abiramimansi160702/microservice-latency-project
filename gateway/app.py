from flask import Flask
import requests
import time

app = Flask(__name__)

@app.route("/")
def gateway():

    start_time = time.time()   # start measuring

    time.sleep(1/100)  # simulate gateway processing

    response = requests.get("http://payment:5001/process")

    end_time = time.time()   # stop measuring

    latency = end_time - start_time

    return f"Gateway → {response.text} | Total Latency: {latency:.4f} seconds"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)