class RankingProbabilityModel:
    def __init__(self):
        pass

    def score(self, competition_score, on_page_score, technical_score):
        weighted_score = (competition_score * 0.5) + (on_page_score * 0.3) + (technical_score * 0.2)
        
        probability = "Low"
        if weighted_score > 80:
            probability = "High"
        elif weighted_score > 60:
            probability = "Medium"
            
        return {
            "score": round(weighted_score, 2),
            "probability": probability,
            "disclaimer": "DISCLAIMER: Google rankings are NEVER guaranteed."
        }

    def evaluate_serp_weakness(self, results):
        weakness_signals = 0
        for r in results:
            if "reddit.com" in r['url'] or "quora.com" in r['url'] or "medium.com" in r['url']:
                weakness_signals += 1
            if len(r['title']) < 30:
                weakness_signals += 0.5
        
        return min(100, weakness_signals * 20)
