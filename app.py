from flask import Flask, render_template, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/health")
def health():
    response = {
        "status": "UP",
        "time": datetime.datetime.utcnow().isoformat() + "Z",
        "hostname": socket.gethostname()
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
