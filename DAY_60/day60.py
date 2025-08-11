import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, save_folder="DAY_60/downloaded_images"):
    # Create  the file for download imag
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # send the requst
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  #Error in http
    except requests.exceptions.RequestException as e:
        print(f"Error in requests: {e}")
        return

   
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    if not img_tags:
        print("No exit image in web site")
        return

   # download the one by one image
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue

        img_url = urljoin(url, img_url)

        try:
            img_data = requests.get(img_url, headers=headers).content
            img_name = os.path.join(save_folder, os.path.basename(img_url))
            
            with open(img_name, 'wb') as f:
                f.write(img_data)
            print(f"دانلود شد: {img_name}")
        except Exception as e:
            print(f"Error in download{img_url}: {e}")

if __name__ == "__main__":
    target_url = "https://taw-bio.ir/f/tag/image/%D8%A7%D9%86%DB%8C%D9%85%D9%87~1~all~bst"  # addres here :))))
    download_images(target_url)