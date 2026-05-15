from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory database simulation
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

orders = []

@app.route('/')
def home():
    return jsonify({
        "app": "E-Commerce API",
        "version": "4.0",
        "server": "192.168.47.152",
        "endpoints": ["/users", "/orders", "/health", "/info"]
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "4.0",
        "timestamp": datetime.now().isoformat(),
        "database": "connected"
    })

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users, "count": len(users)})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/orders', methods=['GET', 'POST'])
def handle_orders():
    if request.method == 'GET':
        return jsonify({"orders": orders, "count": len(orders)})
    
    if request.method == 'POST':
        data = request.get_json()
        order = {
            "id": len(orders) + 1,
            "user_id": data.get("user_id"),
            "product": data.get("product"),
            "amount": data.get("amount"),
            "timestamp": datetime.now().isoformat()
        }
        orders.append(order)
        return jsonify({"message": "Order created", "order": order}), 201

@app.route('/info')
def info():
    return jsonify({
        "app": "E-Commerce API",
        "version": "4.0",
        "deployed_from": "local-server-192.168.47.152",
        "pipeline": "GitHub → Control Plane → PR → DR",
        "features": ["User Management", "Order Processing", "Health Monitoring"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
