from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Jenkins CI/CD Project! and docker push and deploy and Testing"

@app.route("/health")
def health():
    return "Application is Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)