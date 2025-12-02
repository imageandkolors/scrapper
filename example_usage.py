#!/usr/bin/env python3
"""
Example usage of the Lead Finder API
Run this after starting the server with: python run.py
"""
import requests
import time
import json

# API base URL
BASE_URL = "http://localhost:8000"

def check_health():
    """Check if the API is running"""
    response = requests.get(f"{BASE_URL}/health")
    print("Health Check:", response.json())
    return response.status_code == 200

def run_scrape(query, max_results=10):
    """Run a scraping job"""
    print(f"\n🔍 Scraping: {query}")
    print("This may take 1-2 minutes...")
    
    response = requests.post(
        f"{BASE_URL}/api/scrape",
        json={
            "query": query,
            "max_results": max_results
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Success! Found {data['count']} businesses")
        return data
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return None

def get_leads(min_score=60):
    """Get high-scoring leads"""
    response = requests.get(f"{BASE_URL}/api/leads?min_score={min_score}")
    
    if response.status_code == 200:
        leads = response.json()
        print(f"\n📊 Found {len(leads)} leads with score >= {min_score}")
        return leads
    else:
        print(f"❌ Error: {response.status_code}")
        return []

def display_lead(lead):
    """Display a single lead"""
    print("\n" + "="*60)
    print(f"🏢 {lead['name']}")
    print("="*60)
    print(f"Category: {lead.get('category', 'N/A')}")
    print(f"Address: {lead.get('address', 'N/A')}")
    print(f"Phone: {lead.get('phone', 'N/A')}")
    print(f"Website: {lead.get('website', 'NO WEBSITE ⚠️')}")
    print(f"Rating: {lead.get('rating', 'N/A')} ⭐ ({lead.get('review_count', 0)} reviews)")
    print(f"\n🎯 Lead Score: {lead['lead_score']}/100")
    
    if lead.get('audit_summary') and lead['audit_summary'].get('issues'):
        print("\n⚠️  Issues Found:")
        for issue in lead['audit_summary']['issues']:
            print(f"  • {issue}")

def get_business_details(business_id):
    """Get full details for a business"""
    response = requests.get(f"{BASE_URL}/api/business/{business_id}")
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Error: {response.status_code}")
        return None

def export_leads(min_score=60, filename="leads.csv"):
    """Export leads to CSV"""
    response = requests.get(f"{BASE_URL}/api/export?min_score={min_score}")
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"\n💾 Exported to {filename}")
        return True
    else:
        print(f"❌ Export failed: {response.status_code}")
        return False

def main():
    """Example workflow"""
    print("="*60)
    print("Lead Finder - API Example")
    print("="*60)
    
    # 1. Check if API is running
    if not check_health():
        print("❌ API is not running. Start it with: python run.py")
        return
    
    # 2. Run a scrape
    query = "coffee shops in Seattle"
    result = run_scrape(query, max_results=5)
    
    if not result:
        return
    
    # Wait a moment for processing
    time.sleep(2)
    
    # 3. Get leads
    leads = get_leads(min_score=60)
    
    if not leads:
        print("\n😔 No leads found. Try a different search query.")
        return
    
    # 4. Display top 3 leads
    print("\n🏆 Top Leads:")
    for lead in leads[:3]:
        display_lead(lead)
    
    # 5. Get detailed info for first lead
    if leads:
        print("\n" + "="*60)
        print("📋 Detailed Audit for Top Lead")
        print("="*60)
        details = get_business_details(leads[0]['id'])
        if details:
            print(json.dumps(details, indent=2))
    
    # 6. Export to CSV
    export_leads(min_score=60, filename="my_leads.csv")
    
    print("\n✅ Done! Check my_leads.csv for the full list.")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ Could not connect to API.")
        print("Make sure the server is running: python run.py")
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user")
