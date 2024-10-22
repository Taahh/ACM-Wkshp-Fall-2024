from flask import Flask, request
import json

todos = []

app = Flask(__name__)
app.debug = True


@app.route("/", methods=["GET"])
def get_test():
    # Get Parameters usng request.args (dict)
    return json.dumps(todos)

@app.route("/", methods=["POST"])
def post_test():
    # Get Body using request.data or request.get_json()
    # Check Content Type
    # Check if they specified JSON data
    # Check if they provided a valid operation ("add" or "remove")
    if request.content_type != "application/json":
        return "Specify header Content-Type=application/json\n"
    data = {}
    try:
        data = request.get_json()
    except:
        if not data:
            return "Invalid Option, provide JSON data that looks similar to {'add': 'adding', 'remove': 'removing'}\n"

    valid_option = False
    if "add" in data:
        todos.append(data["add"])
        valid_option = True
    if "remove" in data:
        if data["remove"] in todos:
            todos.remove(data["remove"])
        valid_option = True
    if not valid_option:
        return "Invalid Option, provide JSON data that looks similar to {'add': 'adding', 'remove': 'removing'}\n"
    return "ToDo Updated\n"

app.run(port=3001)