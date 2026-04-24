from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

attendance = []

@app.route("/")
def home():
    return "Attendance Backend Running"

@app.route("/mark", methods=["POST"])
def mark():
    data = request.get_json()
    name = data.get("name")

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = {
        "name": name,
        "time": time
    }

    attendance.append(record)

    return jsonify({"message": f"{name} marked at {time}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)