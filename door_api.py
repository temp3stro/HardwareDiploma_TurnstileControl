#!/usr/bin/env python3
import os
import time
from flask import Flask, request, abort, jsonify
from gpiozero import OutputDevice

# Settings
RELAY_PIN = 17
API_TOKEN = os.getenv("DOOR_API_TOKEN", "change_me")

relay = OutputDevice(RELAY_PIN, active_high=True, initial_value=False)
app = Flask(__name__)

def open_door(duration=2.0):
    relay.on()
    time.sleep(duration)
    relay.off()

@app.route("/open", methods=["POST"])
def open_endpoint():
    auth = request.headers.get("Authorization", "")
    if auth != f"Bearer {API_TOKEN}":
        abort(401)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Door open requested")
    open_door(2.0)
    return jsonify({"status": "opened"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
