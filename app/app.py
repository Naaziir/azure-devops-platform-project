from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Azure DevOps Platform Project",
        "status": "running",
        "engineer": "Nazir Saloha"
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)