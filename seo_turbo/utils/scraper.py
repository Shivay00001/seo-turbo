import requests
import time
import random
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, use_proxy=False):
        self.headers = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        ]
        self.use_proxy = use_proxy

    def get_headers(self):
        return {"User-Agent": random.choice(self.headers)}

    def fetch_url(self, url, delay=True):
        if delay:
            time.sleep(random.uniform(1, 3))
        
        try:
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            return None

    def get_soup(self, html):
        if html:
            return BeautifulSoup(html, 'lxml')
        return None
