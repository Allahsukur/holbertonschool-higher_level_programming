#!/usr/bin/python3
"""
Test script for the secure Flask API
"""
import requests
import json
import base64

# API base URL
BASE_URL = "http://localhost:5000"

def test_basic_authentication():
    """
    Test basic authentication functionality
    """
    print("=== Testing Basic Authentication ===")
    
    # Test without credentials (should fail)
    print("\n1. Testing /basic-protected without credentials:")
    response = requests.get(f"{BASE_URL}/basic-protected")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Test with valid credentials
    print("\n2. Testing /basic-protected with valid credentials:")
    credentials = base64.b64encode(b"user1:password").decode('utf-8')
    headers = {'Authorization': f'Basic {credentials}'}
    response = requests.get(f"{BASE_URL}/basic-protected", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Test with invalid credentials
    print("\n3. Testing /basic-protected with invalid credentials:")
    credentials = base64.b64encode(b"user1:wrongpassword").decode('utf-8')
    headers = {'Authorization': f'Basic {credentials}'}
    response = requests.get(f"{BASE_URL}/basic-protected", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


def test_jwt_authentication():
    """
    Test JWT authentication functionality
    """
    print("\n=== Testing JWT Authentication ===")
    
    # Test login with valid credentials
    print("\n1. Testing /login with valid credentials:")
    login_data = {"username": "user1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        
        # Test JWT protected route with valid token
        print("\n2. Testing /jwt-protected with valid token:")
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        # Test JWT protected route without token
        print("\n3. Testing /jwt-protected without token:")
        response = requests.get(f"{BASE_URL}/jwt-protected")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        # Test JWT protected route with invalid token
        print("\n4. Testing /jwt-protected with invalid token:")
        headers = {'Authorization': 'Bearer invalid_token'}
        response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    
    # Test login with invalid credentials
    print("\n5. Testing /login with invalid credentials:")
    login_data = {"username": "user1", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


def test_role_based_access():
    """
    Test role-based access control
    """
    print("\n=== Testing Role-Based Access Control ===")
    
    # Test admin login
    print("\n1. Testing admin login:")
    login_data = {"username": "admin1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        admin_token = response.json().get('access_token')
        
        # Test admin access to admin-only route
        print("\n2. Testing admin access to /admin-only:")
        headers = {'Authorization': f'Bearer {admin_token}'}
        response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    
    # Test regular user login
    print("\n3. Testing regular user login:")
    login_data = {"username": "user1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        user_token = response.json().get('access_token')
        
        # Test regular user access to admin-only route (should fail)
        print("\n4. Testing regular user access to /admin-only (should fail):")
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


def test_additional_endpoints():
    """
    Test additional endpoints
    """
    print("\n=== Testing Additional Endpoints ===")
    
    # Test home endpoint
    print("\n1. Testing home endpoint:")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Test users endpoint with authentication
    print("\n2. Testing /users endpoint:")
    login_data = {"username": "user1", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f"{BASE_URL}/users", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    
    # Test profile endpoint
    print("\n3. Testing /profile endpoint:")
    if response.status_code == 200:
        response = requests.get(f"{BASE_URL}/profile", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


def main():
    """
    Main function to run all tests
    """
    print("Starting Secure Flask API Tests")
    print("=" * 50)
    
    try:
        # Test basic authentication
        test_basic_authentication()
        
        # Test JWT authentication
        test_jwt_authentication()
        
        # Test role-based access control
        test_role_based_access()
        
        # Test additional endpoints
        test_additional_endpoints()
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Flask API.")
        print("Make sure the API is running on http://localhost:5000")
        print("Run: python task_05_basic_security.py")
    except Exception as e:
        print(f"Error during testing: {e}")


if __name__ == "__main__":
    main() 