import argparse
import sys
import os
from rich.console import Console
from rich.panel import Panel

from .engine.keyword_intelligence import KeywordIntelligence
from .engine.on_page_optimizer import OnPageOptimizer
from .engine.technical_checks import TechnicalChecks
from .engine.ranking_model import RankingProbabilityModel
from .utils.reporter import Reporter
from .utils.scraper import Scraper

console = Console()

def main():
    parser = argparse.ArgumentParser(description="SEO Turbo: Python SEO Automation Tool")
    parser.add_argument("--keyword", type=str, required=True, help="Target keyword to analyze")
    parser.add_argument("--url", type=str, help="Existing URL to optimize (optional)")
    parser.add_argument("--out", type=str, default="reports", help="Output directory for reports")
    
    args = parser.parse_args()

    console.print(Panel(f"[bold blue]SEO Turbo[/bold blue]\nStarting analysis for: [green]{args.keyword}[/green]", expand=False))

    # 1. Keyword Intel
    ki = KeywordIntelligence()
    intel = ki.analyze(args.keyword)
    
    # 2. Competitor Weakness
    model = RankingProbabilityModel()
    weakness_score = model.evaluate_serp_weakness(intel['results'])
    
    # 3. Content Analysis
    optimizer = OnPageOptimizer()
    html_content = ""
    on_page_results = {}
    
    if args.url:
        scraper = Scraper()
        html_content = scraper.fetch_url(args.url)
        on_page_results = optimizer.analyze_content(html_content, args.keyword)
    else:
        # Generic content analysis if no URL provided
        on_page_results = {
            "suggestions": ["Include target keyword in H1", "Add meta description"],
            "score": 50
        }
    
    # 4. Tech Checks
    tech_checks = TechnicalChecks()
    tech_results = tech_checks.run_all(html_content if html_content else "<html></html>", args.url)
    
    # 5. Final Scoring
    final_score = model.score(
        competition_score=intel['competition_score'],
        on_page_score=on_page_results.get('score', 80),
        technical_score=80
    )
    
    # Combine Data
    report_data = {
        "keyword": args.keyword,
        "competition_score": intel['competition_score'],
        "probability": final_score['probability'],
        "score": final_score['score'],
        "suggestions": on_page_results.get('suggestions', []),
        "technical": tech_results,
        "disclaimer": final_score['disclaimer']
    }
    
    # 6. Reporting
    reporter = Reporter(output_dir=args.out)
    json_path = reporter.generate_json_report(report_data)
    html_path = reporter.generate_html_report(report_data)
    
    console.print(f"\n[bold green]Success![/bold green] Analysis complete.")
    console.print(f"Ranking Probability: [bold]{final_score['probability']}[/bold]")
    console.print(f"JSON Report: [cyan]{json_path}[/cyan]")
    console.print(f"HTML Report: [cyan]{html_path}[/cyan]")
    
    console.print("\n[dim]" + final_score['disclaimer'] + "[/dim]")

if __name__ == "__main__":
    main()
