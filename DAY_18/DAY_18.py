from datetime import datetime
import json

now = datetime.now()

data = {
    "current_datetime": now.isoformat(),  
    "year": now.year,
    "month": now.month,
    "day": now.day,
    "hour": now.hour,
    "minute": now.minute,
    "second": now.second

}

with open('datetime_info.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Insertt the informetion in datatime_info.json")

