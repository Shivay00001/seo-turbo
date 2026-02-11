from ..utils.scraper import Scraper
import re

class KeywordIntelligence:
    def __init__(self):
        self.scraper = Scraper()

    def search_google(self, keyword):
        query = keyword.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}&num=20"
        html = self.scraper.fetch_url(url)
        return html

    def parse_serp(self, html):
        soup = self.scraper.get_soup(html)
        if not soup:
            return []

        results = []
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text if g.find('h3') else "No Title"
                snippet = g.find('div', class_='VwiC3b').text if g.find('div', class_='VwiC3b') else ""
                
                # Basic check for link quality/domain
                is_major_site = any(domain in link for domain in ['wikipedia.org', 'facebook.com', 'amazon.com', 'microsoft.com'])
                
                results.append({
                    "url": link,
                    "title": title,
                    "snippet": snippet,
                    "is_major_site": is_major_site
                })
        return results

    def calculate_competition_score(self, results):
        if not results:
            return 0
        
        major_sites_count = sum(1 for r in results if r['is_major_site'])
        score = 100 - (major_sites_count * 10)
        return max(0, min(100, score))

    def analyze(self, keyword):
        html = self.search_google(keyword)
        results = self.parse_serp(html)
        score = self.calculate_competition_score(results)
        
        return {
            "keyword": keyword,
            "competition_score": score,
            "results": results
        }
