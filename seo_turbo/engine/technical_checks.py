import time
import requests
from bs4 import BeautifulSoup

class TechnicalChecks:
    def __init__(self):
        pass

    def check_html_size(self, html):
        size_kb = len(html.encode('utf-8')) / 1024
        return {
            "size_kb": round(size_kb, 2),
            "status": "Good" if size_kb < 100 else "Warning" if size_kb < 200 else "Poor"
        }

    def scan_render_blocking(self, html):
        soup = BeautifulSoup(html, 'lxml')
        scripts = soup.find_all('script', src=True)
        blocking = [s['src'] for s in scripts if not s.has_attr('async') and not s.has_attr('defer')]
        return {
            "count": len(blocking),
            "files": blocking[:5]
        }

    def run_all(self, html, url=None):
        return {
            "html_size": self.check_html_size(html),
            "render_blocking": self.scan_render_blocking(html)
        }
