from flask import Flask, request

todos = []

app = Flask(__name__)
app.debug = True


@app.route("/", methods=["GET"])
def get_test():
    # Get Parameters usng request.args (dict)
    return "Test Get"

@app.route("/", methods=["POST"])
def post_test():
    # Get Body using request.data or request.get_json()
    print(request.get_json())
    return "Test Post\n"

app.run(port=3001)