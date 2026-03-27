from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from DevOps Pipeline!</h1>"

@app.route("/about")
def about():
    return "<h1>This app was built using Jenkins CI/CD Pipeline</h1>"

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": "1.0.0",
        "message": "Flask app is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
