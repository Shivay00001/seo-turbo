import os

class IndexingOptimizer:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def generate_xml_sitemap(self, urls, output_path="sitemap.xml"):
        content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for url in urls:
            full_url = f"{self.base_url}/{url.lstrip('/')}"
            content += f'  <url>\n    <loc>{full_url}</loc>\n    <changefreq>daily</changefreq>\n  </url>\n'
        content += "</urlset>"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path

    def generate_robots_txt(self, sitemap_url=None, output_path="robots.txt"):
        content = "User-agent: *\nAllow: /\n"
        if sitemap_url:
            content += f"Sitemap: {sitemap_url}\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path

    def generate_html_sitemap(self, urls, output_path="sitemap.html"):
        content = "<!DOCTYPE html><html><head><title>Sitemap</title></head><body>\n"
        content += "<h1>Sitemap</h1><ul>\n"
        for url in urls:
            full_url = f"{self.base_url}/{url.lstrip('/')}"
            content += f'  <li><a href="{full_url}">{url}</a></li>\n'
        content += "</ul></body></html>"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path

    def get_indexing_api_docs(self):
        return "Google Indexing API Doc Placeholder"
