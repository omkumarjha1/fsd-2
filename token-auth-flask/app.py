from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "mysecretkey"

# Dummy user
USER = {
    "username": "admin",
    "password": "1234"
}

# 1. Authorization Header (Basic-like)
@app.route('/auth-header', methods=['POST'])
def auth_header():
    auth = request.authorization
    if auth and auth.username == USER["username"] and auth.password == USER["password"]:
        return jsonify({"message": "Authenticated via Authorization Header"})
    return jsonify({"message": "Unauthorized"}), 401


# 2. Custom Header
@app.route('/custom-header', methods=['POST'])
def custom_header():
    username = request.headers.get('X-Username')
    password = request.headers.get('X-Password')

    if username == USER["username"] and password == USER["password"]:
        return jsonify({"message": "Authenticated via Custom Header"})
    return jsonify({"message": "Unauthorized"}), 401


# 3. JWT Token Generation
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    if data['username'] == USER["username"] and data['password'] == USER["password"]:
        token = jwt.encode({
            'user': data['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401


# 4. Protected Route (JWT)
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"message": "Token missing"}), 403

    try:
        token = token.split(" ")[1]
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": "Access granted", "user": data['user']})

    except:
        return jsonify({"message": "Invalid token"}), 403


if __name__ == "__main__":
    app.run(debug=True)