import json

class SchemaGenerator:
    def __init__(self):
        pass

    def generate_article_schema(self, title, author, date_published, url, image_url=None):
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "author": {
                "@type": "Person",
                "name": author
            },
            "datePublished": date_published,
            "url": url
        }
        if image_url:
            schema["image"] = image_url
        return json.dumps(schema, indent=2)

    def generate_faq_schema(self, questions_answers):
        main_entity = []
        for q, a in questions_answers:
            main_entity.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })
        
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": main_entity
        }
        return json.dumps(schema, indent=2)
