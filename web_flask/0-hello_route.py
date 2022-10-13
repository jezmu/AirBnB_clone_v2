"""Runs simple flask application with / route only"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Home route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
