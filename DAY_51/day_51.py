import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class HTMLLinkExtractor:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def extract_links(self, html_file):
        """Extract all links from an HTML file with optional filtering"""
        if not os.path.exists(html_file):
            raise FileNotFoundError(f"HTML file not found: {html_file}")

        with open(html_file, 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')

        links = []
        for link in soup.find_all('a', href=True):
            href = link['href'].strip()
            if self._is_valid_link(href):
                if self.base_url and not href.startswith(('http', '//')):
                    href = urljoin(self.base_url, href)
                links.append(href)

        return list(dict.fromkeys(links))  # Remove duplicates while preserving order

    def _is_valid_link(self, href):
        """Filter out unwanted links"""
        return (href 
                and href != '#' 
                and not href.startswith(('javascript:', 'mailto:', 'tel:')))
    
    @staticmethod
    def save_links(links, output_file="links.txt"):
        """Save links to a text file"""
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(links))
        return True

if __name__ == "__main__":
    try:
        # Example usage
        extractor = HTMLLinkExtractor(base_url="https://example.com")
        html_path = "E:/100Days_python/DAY_51/about.html"
        
        links = extractor.extract_links(html_path)
        extractor.save_links(links)
        
        print(f"✅ Successfully extracted {len(links)} links and saved to links.txt")
        print("Sample links:")
        for i, link in enumerate(links[:5], 1):
            print(f"{i}. {link}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")