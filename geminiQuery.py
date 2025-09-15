from google import genai

API_KEY = "AIzaSyC4bk1DySjdbt37IZ0sL2LlcLzjipz4hXA"
client = genai.Client(api_key = API_KEY)

def query_gemini_with_evidence(headline, body, imageLabels, evidence):
    # Construct evidence block
    evidence_text = ""
    for i, ev in enumerate(evidence, 1):
        evidence_text += f"Evidence {i}:\nTitle: {ev['title']}\nLink: {ev['link']}\nSnippet: {ev['snippet']}\n\n"
    
    print("\nEvidence: ", evidence_text)

    prompt = f"""
    You are a fact-checking AI. You will be provided with a news article headline, body and supporting, along with multiple external evidence snippets (from trusted sources).
    Based ONLY on the evidence provided, determine if the article is TRUE, FALSE, or UNKNOWN.
    
    Headline: {headline}
    Body: {body}
    Image Labels: {imageLabels}
    
    External Evidence:
    {evidence_text}
    
    If there is no evidence, treat it as a false claim.
    
    Verdict (TRUE / FALSE / UNKNOWN), and briefly explain your reasoning in not more than 15 words.
    """
    gemini_response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents = prompt
    )

    return gemini_response.text