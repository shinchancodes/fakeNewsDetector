import requests

def google_search(query, num_results=3):
    API_KEY = "AIzaSyBDSld31LYta1jb28sXG2rJda5bthvSUnA"
    SEARCH_ENGINE_ID = "442f139add0984a46"
    
    url = "https://www.googleapis.com/customsearch/v1"
    
    trusted_sites = [ "https://aninews.in/"]
    site_query = " OR ".join([f"site:{site}" for site in trusted_sites])

    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': f"{query} {site_query}",
        'num': num_results
    }
    
    response = requests.get(url, params=params)
    results = response.json()
    
    evidence = []
    
    if 'items' in results:
        for item in results['items']:
            evidence.append({
                'title': item['title'],
                'link': item['link'],
                'snippet': item['snippet']
            })
    
    return evidence