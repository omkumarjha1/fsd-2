from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Dummy customer data
customers = {
    1: {"name": "Om", "orders": [101, 102]}
}

ORDER_SERVICE_URL = "http://127.0.0.1:5001"

@app.route('/customer/<int:id>/orders', methods=['GET'])
def get_customer_orders(id):
    customer = customers.get(id)

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    orders = []
    for order_id in customer["orders"]:
        res = requests.get(f"{ORDER_SERVICE_URL}/order/{order_id}")
        if res.status_code == 200:
            orders.append(res.json())

    return jsonify({
        "customer": customer["name"],
        "orders": orders
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)