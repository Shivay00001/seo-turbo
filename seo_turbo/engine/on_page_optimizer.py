import re
from bs4 import BeautifulSoup

class OnPageOptimizer:
    def __init__(self):
        pass

    def calculate_readability(self, text):
        words = len(re.findall(r'\w+', text))
        sentences = len(re.findall(r'[.!?]+', text))
        if sentences == 0: return 0
        avg_sentence_len = words / sentences
        
        if avg_sentence_len < 15: return "High"
        if avg_sentence_len < 25: return "Medium"
        return "Low"

    def analyze_content(self, html, target_keyword):
        soup = BeautifulSoup(html, 'lxml')
        title = soup.title.string if soup.title else ""
        h1 = [h.text for h in soup.find_all('h1')]
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        meta_desc = meta_desc['content'] if meta_desc else ""
        
        suggestions = []
        if target_keyword.lower() not in title.lower():
            suggestions.append("Incorporate target keyword into Title tag.")
        
        if not h1:
            suggestions.append("Add an H1 tag with your primary keyword.")
        elif target_keyword.lower() not in h1[0].lower():
            suggestions.append("Incorporate target keyword into the first H1 tag.")

        images_missing_alt = [img for img in soup.find_all('img') if not img.get('alt')]
        if images_missing_alt:
            suggestions.append(f"Add ALT tags to {len(images_missing_alt)} images.")

        return {
            "title": title,
            "meta_description": meta_desc,
            "h1": h1,
            "readability": self.calculate_readability(soup.get_text()),
            "suggestions": suggestions
        }
