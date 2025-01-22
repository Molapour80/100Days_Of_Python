import os

def list_files(directory):
    """List files and directories in a specified path."""
    print(f"Contents of {directory}:")
    for item in os.listdir(directory):
        print(item)

def move_file(source, destination):
    """Move a file from one path to another."""
    try:
        os.rename(source, os.path.join(destination, os.path.basename(source)))
        print(f"File {source} moved to {destination}.")
    except Exception as e:
        print(f"Error moving file: {e}")

def delete_file(file_path):
    """Delete a specified file."""
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def create_directory(directory_name):
    """Create a new directory."""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory {directory_name} created.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def main():
    while True:
        print("\nFile Management")
        print("1. List Files")
        print("2. Move File")
        print("3. Delete File")
        print("4. Create Directory")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            dir_path = input("Enter the directory path: ")
            list_files(dir_path)
        elif choice == '2':
            source = input("Enter the source file path: ")
            destination = input("Enter the destination directory path: ")
            move_file(source, destination)
        elif choice == '3':
            file_path = input("Enter the file path: ")
            delete_file(file_path)
        elif choice == '4':
            dir_name = input("Enter the directory name: ")
            create_directory(dir_name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()