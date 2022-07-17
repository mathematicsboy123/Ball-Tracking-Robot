import time
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import static.img as img

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        img.detect_ball()
        time.sleep(5)
        value = request.form.get("input")
        print(value)
        return render_template("index.html", number = value)
    else:
        return render_template("index.html", number = 50)
