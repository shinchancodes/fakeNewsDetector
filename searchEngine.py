import requests

def google_search(query, num_results=3):
    API_KEY = "AIzaSyBDSld31LYta1jb28sXG2rJda5bthvSUnA"
    SEARCH_ENGINE_ID = "442f139add0984a46"
    
    url = "https://www.googleapis.com/customsearch/v1"
    
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
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