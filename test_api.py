#!/usr/bin/env python3
"""
Test script for the PDF Extractor API
"""

import requests
import json

# Test URLs
TEST_URLS = [
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "https://www.ammc.ma/sites/default/files/2024-04/ETATS_FINANCIERS_WAFACASH_2023.pdf"
]

API_BASE = "http://localhost:8080"

def test_health():
    """Test the health endpoint"""
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE}/")
        print(f"✅ Health check: {response.status_code} - {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_extract(pdf_url):
    """Test the extract endpoint with a PDF URL"""
    print(f"\n🔍 Testing extract with: {pdf_url}")
    try:
        payload = {"pdf_url": pdf_url}
        response = requests.post(
            f"{API_BASE}/extract",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Extract successful!")
            print(f"   Text length: {len(data.get('text', ''))}")
            print(f"   Tables found: {len(data.get('tables', []))}")
            print(f"   Status: {data.get('status', 'unknown')}")
            
            # Show first 200 characters of text
            text_preview = data.get('text', '')[:200]
            print(f"   Text preview: {text_preview}...")
            
            return True
        else:
            print(f"❌ Extract failed: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Extract error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting PDF Extractor API Tests\n")
    
    # Test health
    if not test_health():
        print("\n❌ Health check failed. Make sure the API is running on localhost:8080")
        return
    
    # Test extract with each URL
    success_count = 0
    for url in TEST_URLS:
        if test_extract(url):
            success_count += 1
    
    print(f"\n📊 Test Results: {success_count}/{len(TEST_URLS)} tests passed")
    
    if success_count == len(TEST_URLS):
        print("🎉 All tests passed! Your API is ready for deployment.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()
