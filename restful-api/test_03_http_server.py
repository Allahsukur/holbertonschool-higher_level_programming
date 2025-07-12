#!/usr/bin/python3
"""
Test script for the simple HTTP server
"""
import requests
import json
import time


def test_endpoints(base_url="http://localhost:8000"):
    """
    Test all endpoints of the simple HTTP server
    """
    print("Testing Simple HTTP Server Endpoints")
    print("=" * 40)
    
    # Test root endpoint
    print("\n1. Testing root endpoint (/)")
    try:
        response = requests.get(f"{base_url}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Make sure the server is running.")
        return
    
    # Test data endpoint
    print("\n2. Testing data endpoint (/data)")
    try:
        response = requests.get(f"{base_url}/data")
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('content-type')}")
        print(f"Response: {response.text}")
        
        # Parse JSON response
        if response.status_code == 200:
            data = response.json()
            print(f"Parsed JSON: {data}")
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
    
    # Test info endpoint
    print("\n4. Testing info endpoint (/info)")
    try:
        response = requests.get(f"{base_url}/info")
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('content-type')}")
        print(f"Response: {response.text}")
        
        # Parse JSON response
        if response.status_code == 200:
            info = response.json()
            print(f"Parsed JSON: {info}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test undefined endpoint (should return 404)
    print("\n5. Testing undefined endpoint (/nonexistent)")
    try:
        response = requests.get(f"{base_url}/nonexistent")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Make sure the server is running first!")
    print("Run: python3 simple_http_server.py")
    print("\nWaiting 2 seconds before testing...")
    time.sleep(2)
    
    test_endpoints() 