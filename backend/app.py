from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Flask backend is running"
    })


@app.route("/api/submit", methods=["POST"])
def submit_form():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No data received"
        }), 400

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({
            "status": "error",
            "message": "Name, email and message are required"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Form submitted successfully",
        "data": {
            "name": name,
            "email": email,
            "message": message
        }
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
