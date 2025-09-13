from geminiQuery import query_gemini_with_evidence
from searchEngine import google_search

def detect_fake_news(headline, body):
    print("[*] Performing Google Custom Search...")
    search_query = f"{headline} {body[:200]}"
    evidence = google_search(search_query)
    
    print("[*] Querying Gemini with evidence to decide...")
    gemini_verdict = query_gemini_with_evidence(headline, body, evidence)
    
    output = {
        'headline': headline,
        'body': body,
        'external_evidence': evidence,
        'gemini_verdict': gemini_verdict
    }
    
    return output