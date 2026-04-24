from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy order data
orders = {
    101: {"item": "Laptop", "status": "Pending"},
    102: {"item": "Phone", "status": "Shipped"}
}

# Get order
@app.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    order = orders.get(id)
    if not order:
        return jsonify({"message": "Order not found"}), 404
    return jsonify(order)

# Update order status
@app.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    if id not in orders:
        return jsonify({"message": "Order not found"}), 404

    data = request.json
    orders[id]["status"] = data.get("status", orders[id]["status"])

    return jsonify({
        "message": "Order updated",
        "order": orders[id]
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)