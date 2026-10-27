from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__)

# Route: Home / Dashboard
@app.route("/")
def index():
    # You can pass dynamic data here (e.g., tournament stats, active matches)
    return render_template("index.html", title="GOJOGLORY - Esports Dashboard")

# Route: Tournament Matches
@app.route("/matches")
def matches():
    return render_template("matches.html", title="Match Verification")

# API Route: Example endpoint to handle match data or point distribution
@app.route("/api/update-score", methods=["POST"])
def update_score():
    data = request.json
    # Add your logic to handle match verification or point distribution here
    return jsonify({"status": "success", "message": "Score updated successfully", "data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)