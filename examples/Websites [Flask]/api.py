from flask import Flask, jsonify, request # import stuff from flask
from datetime import datetime  # Import datetime from datetime

app = Flask(__name__) # Set app

@app.route('/api/example') # Set the route path / name so in this caste {ip}/api/example
def example():
    return jsonify({"sucess": True, "message": "Hello their!, This is an example Endpoint!"}) # What it responds with, why we need the ({}) is so we can respond in the json format

@app.route('/api/time') # Set the route path / name so in this case {ip}/api/time
def time_stamp():
    return jsonify({"sucess": True, "message": "Hello their!", "timestamp": datetime.now()}) # What it responds with! , Read comment on line 8 for more info
# datetime.now() gets the current timestamp

app.run(port=1500, host='0.0.0.0') # Runs the app, port=1500 sets the port to 1500, and host='0.0.0.0' makes it so it runs as a not just local host app!