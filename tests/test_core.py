import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from seo_turbo.engine.ranking_model import RankingProbabilityModel
from seo_turbo.engine.schema_generator import SchemaGenerator

def test_ranking_model():
    model = RankingProbabilityModel()
    result = model.score(90, 90, 90)
    assert result['probability'] == "High"
    assert result['score'] == 90.0

def test_schema_generator():
    gen = SchemaGenerator()
    schema = gen.generate_article_schema("Test", "Author", "2026-02-11", "https://example.com")
    assert '"@type": "Article"' in schema
    assert '"headline": "Test"' in schema

def test_serp_weakness():
    model = RankingProbabilityModel()
    results = [
        {"url": "https://reddit.com/r/seo", "title": "SEO Tips"},
        {"url": "https://example.com/blog", "title": "Short"}
    ]
    weakness = model.evaluate_serp_weakness(results)
    assert weakness > 0
