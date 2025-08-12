import requests
import time
from datetime import datetime



def check_website(url, timeout=10):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        end_time = time.time()
        
        is_up = response.status_code == 200
        response_time = round((end_time - start_time) * 1000, 2)  
        
        return {
            "url": url,
            "status": "UP" if is_up else "DOWN",
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "status": "DOWN",
            "error": str(e),
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

if __name__ == "__main__":
    websites = [
        "https://check-host.net/",
        "https://github.com",
        "https://example.com"
    ]
    
    for site in websites:
        result = check_website(site)
        print(result)