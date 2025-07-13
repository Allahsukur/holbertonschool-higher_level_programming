#!/usr/bin/python3
"""
Secure Flask API implementation with authentication and authorization
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-in-production'
jwt = JWTManager(app)

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()

# In-memory storage for users with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify basic authentication credentials
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@auth.error_handler
def auth_error():
    """
    Handle basic authentication errors
    """
    return jsonify({"error": "Unauthorized"}), 401


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid token
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle fresh token requirement
    """
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/', methods=['GET'])
def home():
    """
    Root endpoint - returns welcome message
    """
    return "Welcome to the Secure Flask API!"


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Basic authentication protected route
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    JWT login endpoint
    """
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    username = data['username']
    password = data['password']
    
    if username in users and check_password_hash(users[username]['password'], password):
        # Create access token with user info
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]['role']}
        )
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT authentication protected route
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Role-based protected route - admin only
    """
    current_user = get_jwt_identity()
    claims = get_jwt()
    
    if claims.get('role') == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """
    Get all users (protected by JWT)
    """
    user_list = []
    for username, user_data in users.items():
        user_list.append({
            "username": user_data['username'],
            "role": user_data['role']
        })
    return jsonify(user_list)


@app.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """
    Get current user profile
    """
    current_user = get_jwt_identity()
    claims = get_jwt()
    
    if current_user in users:
        return jsonify({
            "username": users[current_user]['username'],
            "role": users[current_user]['role']
        })
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True) 