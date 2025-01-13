import os
directory = "E:\100Days_python"
for i in range(0, 101):
    folder_name = f"DAY_{i}"
    os.makedirs(os.path.join(directory, folder_name), exist_ok=True)

print("create the 100 folders")
