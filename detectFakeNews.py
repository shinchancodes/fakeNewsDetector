from geminiQuery import query_gemini_with_evidence
from searchEngine import google_search
from imageSearch import get_image_labels

def detect_fake_news(headline, body, uploadedImageFile):
    print("[*] Performing Google Custom Search...")
    
    imageLabels = get_image_labels(uploadedImageFile)

    if imageLabels is not None:
        imageLabels = " ".join(imageLabels)
    
    print("Image Labels: ", imageLabels)

    search_query = f"{headline} {body[:200]} Image Labels: {imageLabels}"

    evidence = google_search(search_query)

    print("[*] Querying Gemini with evidence to decide...")
    gemini_verdict = query_gemini_with_evidence(headline, body, imageLabels, evidence)
    
    output = {
        'headline': headline,
        'body': body,
        'Image Labels': imageLabels,
        'external_evidence': evidence,
        'gemini_verdict': gemini_verdict
    }
    
    return output