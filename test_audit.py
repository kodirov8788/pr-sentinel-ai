import os

def process_user_data(user_id):
    # SECURITY RISK: Hardcoded API Key
    api_key = "sk-proj-1234567890abcdef1234567890abcdef"
    
    # PERFORMANCE RISK: N+1 Database Query in a loop
    for i in range(10):
        # Pretend this is a DB query
        print(f"Fetching record {i} for user {user_id} using {api_key}")
        
    return {"status": "success"}
