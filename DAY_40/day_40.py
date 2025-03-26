import requests
from tqdm import tqdm

def download_file(url, save_path):
    """
    Downloads a file from the given URL and saves it to the specified path.
    Includes a progress bar to show the download progress.
    """
    try:
        # Send a GET request to the URL with streaming enabled
        response = requests.get(url, stream=True)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the total file size from the response headers
            total_size = int(response.headers.get('content-length', 0))
            
            # Open the file in write-binary mode and initialize the progress bar
            with open(save_path, 'wb') as file, tqdm(
                desc=save_path,  # Description for the progress bar
                total=total_size,  # Total file size
                unit='B',  # Unit of measurement (bytes)
                unit_scale=True,  # Scale the units (KB, MB, etc.)
                unit_divisor=1024,  # Divisor for scaling (1024 for KB, MB, etc.)
            ) as bar:
                # Write the content in chunks and update the progress bar
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    bar.update(len(chunk))  # Update the progress bar
            print(f"File downloaded successfully and saved to {save_path}.")
        elif response.status_code == 404:
            print("Error: The file was not found (404). Please check the URL.")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

# Example usage
if __name__ == "__main__":
    url = "https://www.w3schools.com/html/img_girl.jpg"  # Valid image URL
    save_path = "girl.jpg"   # Path to save the file on your system
    download_file(url, save_path)