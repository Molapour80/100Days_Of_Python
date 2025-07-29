import os
import ctypes
import time
import random
from platform import system

def change_wallpaper(image_path):
    """
    Function to change system wallpaper based on image path
    """
    os_type = system()
    
    try:
        if os_type == "Windows":
            # For Windows
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        elif os_type == "Linux":
            # For Linux (GNOME)
            os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
        elif os_type == "Darwin":
            # For Mac
            os.system(f"""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{image_path}"'""")
        else:
            print("Operating system not supported.")
            return False
        
        print(f"Wallpaper successfully changed to: {image_path}")
        return True
    except Exception as e:
        print(f"Error changing wallpaper: {e}")
        return False

def get_images_from_folder(folder_path):
    """
    Get list of all images from a specific folder
    """
    if not os.path.isdir(folder_path):
        print(f"Folder {folder_path} not found!")
        return []
    
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    images = []
    
    for file in os.listdir(folder_path):
        if any(file.lower().endswith(ext) for ext in valid_extensions):
            images.append(os.path.join(folder_path, file))
    
    return images

def auto_change_wallpaper(folder_path, interval_seconds=60):
    """
    Automatically change wallpaper at specified intervals
    """
    images = get_images_from_folder(folder_path)
    
    if not images:
        print("No suitable images found in the folder.")
        return
    
    print(f"Found {len(images)} images for wallpaper rotation.")
    
    while True:
        try:
            # Randomly select an image
            selected_image = random.choice(images)
            print(f"Changing wallpaper to: {selected_image}")
            
            # Change the wallpaper
            change_wallpaper(selected_image)
            
            # Wait for specified duration
            time.sleep(interval_seconds)
            
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break
        except Exception as e:
            print(f"Unknown error: {e}")
            time.sleep(5)  # Wait 5 seconds if error occurs

if __name__ == "__main__":
    # Path to folder containing images (change this)
    wallpaper_folder = r"C:\Wallpapers"  # For Windows
    # wallpaper_folder = "/home/user/Wallpapers"  # For Linux
    
    # Wallpaper change interval in seconds (here: every 1 minute)
    change_interval = 60
    
    print("Automatic wallpaper changer started...")
    auto_change_wallpaper(wallpaper_folder, change_interval)