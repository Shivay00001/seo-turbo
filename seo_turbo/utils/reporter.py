import json
import os

class Reporter:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_json_report(self, data, filename="seo_report.json"):
        path = os.path.join(self.output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return path

    def generate_html_report(self, data, filename="seo_report.html"):
        path = os.path.join(self.output_dir, filename)
        html = f"<html><body><h1>SEO Report: {data.get('keyword')}</h1></body></html>"
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return path
