#!/usr/bin/python3
"""
Flask API implementation for user management
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/', methods=['GET'])
def home():
    """
    Root endpoint - returns welcome message
    """
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_data():
    """
    Returns a list of all usernames stored in the API
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status', methods=['GET'])
def get_status():
    """
    Returns API status
    """
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Returns the full object corresponding to the provided username
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary
    """
    data = request.get_json()
    
    # Check if username is provided
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Add user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }
    
    # Return confirmation message with user data
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(debug=True) 