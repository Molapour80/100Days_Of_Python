import os
import shutil
from datetime import datetime
import time

def create_backup(source_file, backup_dir):
    """Create a timestamped backup of the source file."""
    if not os.path.exists(source_file):
        print(f"Error: Source file not found: {source_file}")
        return False
    
    os.makedirs(backup_dir, exist_ok=True)  # Create backup dir if it doesn't exist
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(source_file)
    backup_name = f"{filename}_backup_{timestamp}{os.path.splitext(source_file)[1]}"
    backup_path = os.path.join(backup_dir, backup_name)
    
    try:
        shutil.copy2(source_file, backup_path)
        print(f"✅ Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

def auto_backup(source_file, backup_dir, interval_minutes=60):
    """Run automatic backups at regular intervals."""
    print(f"🔁 Starting backup system for: {source_file}")
    print(f"📂 Backup location: {backup_dir}")
    print(f"⏱ Interval: Every {interval_minutes} minutes")
    
    while True:
        create_backup(source_file, backup_dir)
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    # ✅ Corrected paths (using raw strings)
    SOURCE_FILE = r"C:\Users\pishro-pc\Pictures\Saved Pictures\hello.jpg"
    BACKUP_DIR = r"E:\100Days_python\DAY_56\Backups"
    INTERVAL = 60  # Backup every 60 minutes
    
    auto_backup(SOURCE_FILE, BACKUP_DIR, INTERVAL)