from datetime import datetime
import json
import os

def save_data_to_file(data, file_name):
    """ذخیره داده‌ها در فایل JSON."""
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def read_data_from_file(file_name):
    """خواندن داده‌ها از فایل JSON."""
    with open(file_name, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


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

file_name = "datatime.json"


if not os.path.exists(file_name):
    save_data_to_file(data, file_name)
    print(f"File '{file_name}' created and information saved.")
else:
    print(f"File '{file_name}' exists.")

    try:
        existing_data = read_data_from_file(file_name)
        existing_data.update(data)
        save_data_to_file(existing_data, file_name)
        print(f"Information saved in '{file_name}'.")
    except json.JSONDecodeError:
        print(f"Error reading file '{file_name}'. The file may be corrupted.")
    
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted. Please run the program again.")