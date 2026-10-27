from flask import Flask
import asyncio
import main

app = Flask(__name__)

@app.route("/")
def index():
    return "GOJOGLORY is running!"

if __name__ == "__main__":
    app.run()