from flask import Flask, request, jsonify

app = Flask(__name__)


# Route (endpoint, location on API we go to to get data)
# Path paramter is user_id
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "John Doe",
        "email" : "john.doe@example.com"
    }

    # Query parameter (follows a "?")
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# Most common methods: GET, POST, PUT, DELETE
@app.route("/create-user", methods=["POST"])
def creat_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)