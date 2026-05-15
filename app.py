from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from PR-DR Deployment! Version 3.0 - From Local Server"

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": "3.0", "server": "192.168.47.152"})

@app.route('/info')
def info():
    return jsonify({"app": "pr-dr-demo-app", "deployed": "via GitHub pipeline", "source": "local-server"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
