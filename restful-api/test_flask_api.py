#!/usr/bin/python3
"""
Test script for the Flask API
"""
import requests
import json
import time


def test_flask_api(base_url="http://localhost:5000"):
    """
    Test all endpoints of the Flask API
    """
    print("Testing Flask API Endpoints")
    print("=" * 40)
    
    # Test root endpoint
    print("\n1. Testing root endpoint (/)")
    try:
        response = requests.get(f"{base_url}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Make sure Flask is running.")
        print("Run: flask --app task_04_flask.py run")
        return
    
    # Test data endpoint
    print("\n2. Testing data endpoint (/data)")
    try:
        response = requests.get(f"{base_url}/data")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test status endpoint
    print("\n3. Testing status endpoint (/status)")
    try:
        response = requests.get(f"{base_url}/status")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test get user endpoint - existing user
    print("\n4. Testing get user endpoint (/users/jane)")
    try:
        response = requests.get(f"{base_url}/users/jane")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test get user endpoint - non-existing user
    print("\n5. Testing get user endpoint (/users/nonexistent)")
    try:
        response = requests.get(f"{base_url}/users/nonexistent")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test add user endpoint - valid data
    print("\n6. Testing add user endpoint (/add_user) - valid data")
    try:
        new_user = {
            "username": "alice",
            "name": "Alice",
            "age": 25,
            "city": "San Francisco"
        }
        response = requests.post(f"{base_url}/add_user", json=new_user)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test add user endpoint - missing username
    print("\n7. Testing add user endpoint (/add_user) - missing username")
    try:
        invalid_user = {
            "name": "Bob",
            "age": 35,
            "city": "Chicago"
        }
        response = requests.post(f"{base_url}/add_user", json=invalid_user)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test data endpoint again to see if new user was added
    print("\n8. Testing data endpoint again (/data)")
    try:
        response = requests.get(f"{base_url}/data")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Make sure the Flask server is running first!")
    print("Run: flask --app task_04_flask.py run")
    print("\nWaiting 2 seconds before testing...")
    time.sleep(2)
    
    test_flask_api() 