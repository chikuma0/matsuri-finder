import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
import requests

class MatsuriScraper:
    def __init__(self):
        self.base_urls = {
            'kyoto': 'https://www.kyoto-kankou.or.jp',
            'osaka': 'https://www.osaka-info.jp',
            'tokyo': 'https://www.gotokyo.org'
        }
        
    def scrape_festivals(self):
        festivals = []
        for city, url in self.base_urls.items():
            try:
                print(f"Scraping festivals from {city}")
                # Add city-specific scraping logic here
                city_festivals = self.scrape_city(city, url)
                festivals.extend(city_festivals)
            except Exception as e:
                print(f"Error scraping {city}: {str(e)}")
        
        return festivals

    def save_to_json(self, festivals):
        # Ensure data directory exists
        os.makedirs('data', exist_ok=True)
        
        # Save with timestamp
        timestamp = datetime.now().strftime('%Y%m%d')
        filename = f'data/festivals_{timestamp}.json'
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(festivals, f, ensure_ascii=False, indent=2)
        
        print(f"Saved {len(festivals)} festivals to {filename}")

def main():
    scraper = MatsuriScraper()
    festivals = scraper.scrape_festivals()
    scraper.save_to_json(festivals)

if __name__ == "__main__":
    main()
