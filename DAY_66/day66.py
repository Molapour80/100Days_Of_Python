# -*- coding: utf-8 -*-
"""
Currency and Gold Price Scraper from TGJU
اسکرپر قیمت دلار و طلا از TGJU
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import re


class PriceScraper:
    def __init__(self):
        self.results = []
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    
    def scrape_tgju_prices(self):
        """
        دریافت قیمت دلار و طلا از TGJU
        """
        try:
            print("🔍 در حال دریافت قیمت‌ها از TGJU...")
            
            url = "https://www.tgju.org"
            response = self.session.get(url, headers=self.headers, timeout=15)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # دریافت قیمت دلار
                usd_price = self.extract_usd_price(soup)
                if usd_price:
                    self.results.append({
                        'item': 'دلار',
                        'price': usd_price,
                        'unit': 'تومان',
                        'source': 'TGJU',
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    print(f"✅ قیمت دلار: {usd_price} تومان")
                else:
                    print("❌ قیمت دلار پیدا نشد")
                
                # دریافت قیمت طلا
                gold_price = self.extract_gold_price(soup)
                if gold_price:
                    self.results.append({
                        'item': 'طلا (۱۸ عیار)',
                        'price': gold_price,
                        'unit': 'تومان',
                        'source': 'TGJU',
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    print(f"✅ قیمت طلا: {gold_price} تومان")
                else:
                    print("❌ قیمت طلا پیدا نشد")
                
                return len(self.results) > 0
                
            else:
                print(f"❌ خطا در ارتباط با TGJU: کد {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ خطا در دریافت قیمت‌ها: {e}")
            return False
    
    def extract_usd_price(self, soup):
        """
        استخراج قیمت دلار
        """
        try:
            # روش ۱: جستجوی مستقیم در متن صفحه
            page_text = soup.get_text()
            
            # الگو برای پیدا کردن قیمت‌های بزرگ (قیمت دلار)
            usd_patterns = [
                r'دلار[^\d]*(\d{1,3}(?:,\d{3})*)',
                r'USD[^\d]*(\d{1,3}(?:,\d{3})*)',
                r'price_dollar_rl[^\d]*(\d{1,3}(?:,\d{3})*)'
            ]
            
            for pattern in usd_patterns:
                matches = re.findall(pattern, page_text, re.IGNORECASE)
                if matches:
                    return matches[0]
            
            # روش ۲: جستجو در المان‌های HTML
            usd_elements = soup.find_all(['span', 'td', 'div'], 
                                       string=re.compile(r'\d{1,3}(?:,\d{3})+'))
            
            for element in usd_elements:
                text = element.get_text(strip=True)
                # اگر عدد بزرگی باشد (قیمت دلار)
                if len(text.replace(',', '')) > 4:
                    # بررسی کن که در نزدیکی آن کلمه "دلار" باشد
                    parent_text = element.parent.get_text() if element.parent else ""
                    if 'دلار' in parent_text or 'USD' in parent_text.upper():
                        return text
            
            return None
            
        except Exception as e:
            print(f"خطا در استخراج قیمت دلار: {e}")
            return None
    
    def extract_gold_price(self, soup):
        """
        استخراج قیمت طلا
        """
        try:
            page_text = soup.get_text()
            
            # الگو برای پیدا کردن قیمت طلا
            gold_patterns = [
                r'طلا[^\d]*(\d{1,3}(?:,\d{3})*)',
                r'مثقال[^\d]*(\d{1,3}(?:,\d{3})*)',
                r'عیار[^\d]*(\d{1,3}(?:,\d{3})*)',
                r'gold[^\d]*(\d{1,3}(?:,\d{3})*)',
                r'geram24[^\d]*(\d{1,3}(?:,\d{3})*)'
            ]
            
            for pattern in gold_patterns:
                matches = re.findall(pattern, page_text, re.IGNORECASE)
                if matches:
                    return matches[0]
            
            # جستجو در المان‌های HTML برای قیمت طلا
            gold_elements = soup.find_all(['span', 'td', 'div'], 
                                        string=re.compile(r'\d{1,3}(?:,\d{3})+'))
            
            for element in gold_elements:
                text = element.get_text(strip=True)
                if len(text.replace(',', '')) > 5:  # قیمت طلا معمولاً بزرگتر است
                    parent_text = element.parent.get_text() if element.parent else ""
                    if any(word in parent_text for word in ['طلا', 'مثقال', 'عیار', 'gold']):
                        return text
            
            return None
            
        except Exception as e:
            print(f"خطا در استخراج قیمت طلا: {e}")
            return None
    
    def add_fallback_prices(self):
        """
        افزودن قیمت‌های نمونه در صورت عدم موفقیت
        """
        print("💡 افزودن قیمت‌های نمونه...")
        
        sample_prices = [
            {
                'item': 'دلار',
                'price': '58,500',
                'unit': 'تومان', 
                'source': 'SAMPLE',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                'item': 'طلا (۱۸ عیار)',
                'price': '312,500',
                'unit': 'تومان',
                'source': 'SAMPLE',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                'item': 'یورو',
                'price': '63,200',
                'unit': 'تومان',
                'source': 'SAMPLE', 
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        ]
        
        for price in sample_prices:
            self.results.append(price)
            print(f"✅ {price['item']}: {price['price']} {price['unit']}")
        
        return True
    
    def display_prices(self):
        """
        نمایش قیمت‌ها در کنسول
        """
        if not self.results:
            print("📭 هیچ قیمتی برای نمایش وجود ندارد")
            return
        
        print("\n" + "="*60)
        print("💰 قیمت‌های فعلی بازار")
        print("="*60)
        
        for item in self.results:
            print(f"🏷️  {item['item']}: {item['price']} {item['unit']}")
        
        print("="*60)
    
    def save_to_excel(self, filename="market_prices.xlsx"):
        """
        ذخیره قیمت‌ها در فایل اکسل
        """
        try:
            if not self.results:
                print("⚠️ هیچ داده‌ای برای ذخیره وجود ندارد")
                return False
            
            df = pd.DataFrame(self.results)
            df.to_excel(filename, index=False)
            print(f"💾 قیمت‌ها در فایل {filename} ذخیره شد")
            
            # نمایش جدول در کنسول
            print("\n📊 جدول قیمت‌ها:")
            print(df.to_string(index=False))
            
            return True
            
        except Exception as e:
            print(f"❌ خطا در ذخیره فایل: {e}")
            return False
    
    def run_scraper(self):
        """
        اجرای اصلی اسکرپر
        """
        print("🚀 شروع دریافت قیمت دلار و طلا...")
        print("-" * 50)
        
        # دریافت قیمت‌ها از TGJU
        success = self.scrape_tgju_prices()
        
        # اگر موفق نبود، قیمت‌های نمونه اضافه کن
        if not success or len(self.results) == 0:
            print("🔧 استفاده از داده‌های پشتیبان...")
            self.add_fallback_prices()
        
        # نمایش قیمت‌ها
        self.display_prices()
        
        # ذخیره در فایل
        self.save_to_excel()
        
        return len(self.results) > 0


def main():
    """
    تابع اصلی
    """
    print("🎯 اسکرپر قیمت دلار و طلا")
    print("در حال دریافت آخرین قیمت‌ها از بازار...")
    
    scraper = PriceScraper()
    scraper.run_scraper()
    
    print("\n🎉 عملیات کامل شد!")
    print("فایل market_prices.xlsx را بررسی کنید")


if __name__ == "__main__":
    main()