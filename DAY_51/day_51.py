from bs4 import BeautifulSoup

def extract_links_from_html(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')

    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    
    return links

def save_links_to_file(links, output_file="links.txt"):
    with open(output_file, 'w') as file:
        for link in links:
            file.write(link + '\n')

if __name__ == "__main__":
    html_file = "E:/100Days_python/DAY_51/about.html"
    links = extract_links_from_html(html_file)
    
    save_links_to_file(links)
    print("Save the file :)))")