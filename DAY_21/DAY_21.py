##THIME
import time
from datetime import datetime , timedelta

def create_reminder(reminder_time, message):
    while True:
        current_time = datetime.now()
        if current_time >= reminder_time:
            print(f"🔔 Reminder: {message}")
            break
        time.sleep(1)  # Check every second


def main():
    print("Welcome to the Reminder App!!")

    # Get reminder details from user
    reminder_message = input("Enter your reminder message: ")

    reminder_hour = int(input("Enter hour (0-23): "))
    reminder_minute = int(input("Enter minute (0-59): "))
    
    now =datetime.now()
    reminder_time = now.replace(hour=reminder_hour, minute=reminder_minute, second=0, microsecond=0)
    
    if reminder_time < now:
        reminder_time += timedelta(days=1)

    print(f"Reminder set for {reminder_time}!")
    create_reminder(reminder_time, reminder_message)

if __name__ == "__main__":
    main()
    


