
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)
app.logger.setLevel("INFO")

APP_NAME = "CloudOps Deployment Dashboard"
APP_VERSION = "1.0.0"
ENVIRONMENT = os.getenv("APP_ENV", "Development")


@app.route("/")
def home():
    app.logger.info("Dashboard home page requested")

    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_version=APP_VERSION,
        environment=ENVIRONMENT
    )


@app.route("/health")
def health():
    app.logger.info("Health check endpoint requested")

    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION
    })


@app.route("/api/info")
def api_info():
    app.logger.info("Application information endpoint requested")

    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000))
    )
