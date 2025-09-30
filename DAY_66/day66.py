# -*- coding: utf-8 -*-
"""
Real-time Currency and Gold Price Scraper from TGJU
Fetches live USD and Gold prices from TGJU.org website
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import re


class RealPriceScraper:
    """
    Main class for scraping real-time currency and gold prices from TGJU
    """
    
    def __init__(self):
        # Initialize empty list to store results
        self.results = []
        
        # Create a session for efficient connection reuse
        self.session = requests.Session()
        
        # Set headers to mimic a real browser and avoid blocking
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    
    def scrape_real_tgju_prices(self):
        """
        Scrape real prices from TGJU website by analyzing actual site structure
        Returns: Boolean indicating success
        """
        try:
            print("🔍 Scraping real-time prices from TGJU...")
            
            # Target website URL
            url = "https://www.tgju.org"
            
            # Send GET request to the website
            response = self.session.get(url, headers=self.headers, timeout=15)
            
            # Check if request was successful
            if response.status_code == 200:
                print("✅ Successfully connected to TGJU")
                
                # Parse HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract prices from actual website structure
                prices_found = self.extract_from_actual_structure(soup)
                
                if prices_found:
                    print("✅ Prices successfully extracted from website")
                    return True
                else:
                    print("❌ Could not find prices in website structure")
                    return False
            else:
                print(f"❌ Error connecting to TGJU: Status code {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error scraping prices: {e}")
            return False
    
    def extract_from_actual_structure(self, soup):
        """
        Extract prices from TGJU's actual HTML structure
        Args:
            soup: BeautifulSoup object containing parsed HTML
        Returns: Boolean indicating if prices were found
        """
        try:
            # List to store potential price elements
            price_elements = []
            
            # 1. Search in tables (common structure for price data)
            tables = soup.find_all('table')
            print(f"📊 Number of tables found: {len(tables)}")
            
            # Examine first 5 tables for relevant data
            for i, table in enumerate(tables[:5]):
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    # Combine all cell text in this row
                    row_text = ' '.join([cell.get_text(strip=True) for cell in cells])
                    
                    # Check if row contains currency or gold keywords
                    if any(keyword in row_text for keyword in ['دلار', 'طلا', 'سکه', 'یورو', 'USD', 'Gold']):
                        price_elements.append(row_text)
                        print(f"🔍 Relevant row: {row_text[:100]}...")
            
            # 2. Search in divs with specific classes
            divs = soup.find_all('div', class_=True)
            for div in divs[:20]:  # Check first 20 divs
                div_class = div.get('class', [])
                div_text = div.get_text(strip=True)
                
                # Check if class indicates price-related content
                if any(keyword in str(div_class).lower() for keyword in ['price', 'value', 'num', 'rate']):
                    if len(div_text) > 3 and any(char.isdigit() for char in div_text):
                        price_elements.append(f"DIV: {div_text}")
            
            # 3. Search in span elements
            spans = soup.find_all('span')
            for span in spans[:50]:  # Check first 50 spans
                span_text = span.get_text(strip=True)
                
                # Check if span text looks like a price (large number)
                if len(span_text) > 4 and any(char.isdigit() for char in span_text):
                    # Check for comma-separated numbers or large numbers
                    if any(separator in span_text for separator in ['٬', ',']) or len(span_text.replace(',', '').replace('٬', '')) > 4:
                        # Check if parent element contains currency names
                        parent_text = span.parent.get_text() if span.parent else ""
                        if any(currency in parent_text for currency in ['دلار', 'طلا', 'سکه', 'یورو']):
                            price_elements.append(f"SPAN: {span_text} - Context: {parent_text[:50]}")
            
            print(f"📝 Number of potential price elements found: {len(price_elements)}")
            
            # Process found elements and extract actual prices
            return self.process_found_elements(price_elements)
            
        except Exception as e:
            print(f"❌ Error extracting from structure: {e}")
            return False
    
    def process_found_elements(self, elements):
        """
        Process found elements and extract actual prices
        Args:
            elements: List of potential price-containing elements
        Returns: Boolean indicating if prices were extracted
        """
        try:
            prices_extracted = False
            
            for element in elements:
                element_str = str(element)
                
                # Extract USD price
                if 'دلار' in element_str or 'USD' in element_str.upper():
                    usd_price = self.extract_price_from_text(element_str)
                    if usd_price:
                        self.results.append({
                            'item': 'USD',
                            'price': usd_price,
                            'unit': 'Toman',
                            'source': 'TGJU-Real',
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        print(f"✅ Real USD price: {usd_price} Toman")
                        prices_extracted = True
                
                # Extract Gold price
                if 'طلا' in element_str or 'GOLD' in element_str.upper():
                    gold_price = self.extract_price_from_text(element_str)
                    if gold_price:
                        self.results.append({
                            'item': 'Gold (18K)',
                            'price': gold_price,
                            'unit': 'Toman',
                            'source': 'TGJU-Real',
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        print(f"✅ Real Gold price: {gold_price} Toman")
                        prices_extracted = True
            
            return prices_extracted
            
        except Exception as e:
            print(f"❌ Error processing elements: {e}")
            return False
    
    def extract_price_from_text(self, text):
        """
        Extract price number from text using regex patterns
        Args:
            text: String containing potential price information
        Returns: Extracted price string or None
        """
        try:
            # Pattern to find numbers with commas (like 58,500)
            price_pattern = r'(\d{1,3}(?:[,٬]\d{3})+)'
            matches = re.findall(price_pattern, text)
            
            if matches:
                # Return the largest number (likely the main price)
                return max(matches, key=lambda x: len(x.replace(',', '').replace('٬', '')))
            
            return None
            
        except Exception as e:
            print(f"Error extracting price from text: {e}")
            return None
    
    def scrape_using_api_method(self):
        """
        Alternative method: Use specific price pages or different approaches
        Returns: Boolean indicating success
        """
        try:
            print("🔧 Using alternative method to fetch prices...")
            
            # Try currency-specific page
            price_url = "https://www.tgju.org/currency"
            response = self.session.get(price_url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all large numbers in the page
                large_numbers = []
                for element in soup.find_all(string=True):
                    text = element.strip()
                    if text and any(char.isdigit() for char in text):
                        # Clean and check number size
                        clean_num = text.replace(',', '').replace('٬', '')
                        if clean_num.isdigit() and len(clean_num) > 4:
                            large_numbers.append(text)
                
                print(f"🔢 Large numbers found: {large_numbers[:5]}")
                
                if len(large_numbers) >= 2:
                    # Assume first two large numbers are USD and Gold prices
                    self.results.append({
                        'item': 'USD (Estimated)',
                        'price': large_numbers[0],
                        'unit': 'Toman',
                        'source': 'TGJU-Alternative',
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
                    self.results.append({
                        'item': 'Gold (Estimated)',
                        'price': large_numbers[1], 
                        'unit': 'Toman',
                        'source': 'TGJU-Alternative',
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
                    print(f"✅ Estimated USD price: {large_numbers[0]}")
                    print(f"✅ Estimated Gold price: {large_numbers[1]}")
                    return True
            
            return False
            
        except Exception as e:
            print(f"❌ Error in alternative method: {e}")
            return False
    
    def add_fallback_prices(self):
        """
        Add sample prices only if all scraping methods fail
        Returns: Boolean indicating success
        """
        print("💡 Using fallback data...")
        
        # Sample data for demonstration
        sample_prices = [
            {'item': 'USD', 'price': '58,500', 'unit': 'Toman', 'source': 'SAMPLE'},
            {'item': 'Gold (18K)', 'price': '312,500', 'unit': 'Toman', 'source': 'SAMPLE'},
        ]
        
        for price in sample_prices:
            self.results.append({
                'item': price['item'],
                'price': price['price'],
                'unit': price['unit'],
                'source': price['source'],
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        
        return True
    
    def display_results(self):
        """Display results in console with clear formatting"""
        if not self.results:
            print("📭 No prices retrieved")
            return
        
        print("\n" + "="*60)
        print("💰 Current Market Prices")
        print("="*60)
        
        for item in self.results:
            # Use red indicator for sample data, green for real data
            source_indicator = "🔴" if "SAMPLE" in item['source'] else "🟢"
            print(f"{source_indicator} {item['item']}: {item['price']} {item['unit']} ({item['source']})")
        
        print("="*60)
    
    def save_to_excel(self):
        """Save results to Excel file"""
        try:
            if not self.results:
                print("⚠️ No data to save")
                return False
            
            df = pd.DataFrame(self.results)
            filename = "real_market_prices.xlsx"
            df.to_excel(filename, index=False)
            print(f"💾 Prices saved to {filename}")
            
            print("\n📊 Complete Price Table:")
            print(df.to_string(index=False))
            
            return True
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
            return False
    
    def run_complete_scraper(self):
        """
        Run complete scraping process with multiple fallback methods
        Returns: Boolean indicating overall success
        """
        print("🚀 Starting real-time price scraping...")
        print("-" * 50)
        
        # Method 1: Direct scraping from main structure
        success = self.scrape_real_tgju_prices()
        
        # Method 2: Alternative approach if first method fails
        if not success:
            print("🔄 Trying alternative method...")
            success = self.scrape_using_api_method()
        
        # Method 3: Fallback to sample data if all else fails
        if not success:
            print("🔄 Using fallback data...")
            self.add_fallback_prices()
        
        # Display final results
        self.display_results()
        
        # Save to Excel file
        self.save_to_excel()
        
        return True


def main():
    """
    Main function to run the price scraper
    """
    print("🎯 Real-time USD and Gold Price Scraper")
    print("Fetching live prices from TGJU...")
    print("=" * 50)
    
    # Create scraper instance and run
    scraper = RealPriceScraper()
    scraper.run_complete_scraper()
    
    print("\n🎉 Operation completed!")
    print("Check real_market_prices.xlsx file for results")


# ::::::::Entry point of the script::::::
if __name__ == "__main__":
    main()