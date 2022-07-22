# Written by Shreyans Daga
import time
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Shutdown Flask session from within code
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# Ensure that settings have been set correctly
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Main Page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get users HSV values
        min_h = str(request.form.get("min_h"))
        min_s = str(request.form.get("min_s"))
        min_v = str(request.form.get("min_v"))
        max_h = str(request.form.get("max_h"))
        max_s = str(request.form.get("max_s"))
        max_v = str(request.form.get("max_v"))

        # Write users HSV values into a file
        with open("static/hsv_values.txt", "w") as file:
            file.write(f"{min_h}, {min_s}, {min_v}, {max_h}, {max_s}, {max_v}")

        # Show user main page
        return render_template("index.html", min_h = min_h, min_s = min_s, min_v = min_v, max_h = max_h, max_s = max_s, max_v = max_v)
    else:
        # If user has submitted final HSV values then redirect them to the next page
        if request.args.get("final") == "final":
            return redirect("/complete")
        # If not then just render the main page
        return render_template("index.html", number = 50)

# After user has entered final HSV values
@app.route("/complete", methods=["GET", "POST"])
def complete():
    # Shut down the server and render the final page
    shutdown_server()
    return render_template("complete.html")
