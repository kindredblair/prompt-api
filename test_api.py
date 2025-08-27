#!/usr/bin/env python3
"""
Test script for the Prompt API
Demonstrates how to use the API programmatically
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:8000"
API_KEY = "super-secret-key"

def test_get_persona_prompt():
    """Test getting a specific persona prompt"""
    print("Testing GET /prompts/ellie...")
    
    headers = {"X-API-Key": API_KEY}
    response = requests.get(f"{BASE_URL}/prompts/ellie", headers=headers)
    
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)}")
    else:
        print(f"Error: {response.text}")
    print()

def test_list_all_prompts():
    """Test listing all prompts"""
    print("Testing GET /prompts...")
    
    headers = {"X-API-Key": API_KEY}
    response = requests.get(f"{BASE_URL}/prompts", headers=headers)
    
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Available personas: {list(data.keys())}")
        print(f"Response: {json.dumps(data, indent=2)}")
    else:
        print(f"Error: {response.text}")
    print()

def test_unauthorized_access():
    """Test accessing without API key"""
    print("Testing unauthorized access...")
    
    response = requests.get(f"{BASE_URL}/prompts/ellie")
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    print()

def test_nonexistent_persona():
    """Test accessing a non-existent persona"""
    print("Testing non-existent persona...")
    
    headers = {"X-API-Key": API_KEY}
    response = requests.get(f"{BASE_URL}/prompts/nonexistent", headers=headers)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    print()

if __name__ == "__main__":
    print("=== Prompt API Test Suite ===\n")
    
    test_get_persona_prompt()
    test_list_all_prompts()
    test_unauthorized_access()
    test_nonexistent_persona()
    
    print("=== Test Complete ===")
