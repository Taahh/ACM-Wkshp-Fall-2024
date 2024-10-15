from flask import Flask, request
import json

todos = []

app = Flask(__name__)
app.debug = True


@app.route("/", methods=["GET"])
def get_test():
    # Get Parameters usng request.args (dict)
    return "Test"

@app.route("/", methods=["POST"])
def post_test():
    # Get Body using request.data or request.get_json()
    # Check Content Type
    # Check if they specified JSON data
    # Check if they provided a valid operation ("add" or "remove")
    
    return "ToDo Updated"

app.run(port=3001)