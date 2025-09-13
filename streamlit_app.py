import streamlit as st
from detectFakeNews import detect_fake_news

# Show title and description.
st.title("💬 No Fake News")

headline = st.text_input("Headline")
body = st.text_input("Body")

if st.button("Submit"):
    verdict = detect_fake_news(headline = headline, body = body)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        result = verdict["gemini_verdict"]

        result += "\n=== Top Evidence Links ===\n"
        for i, ev in enumerate(verdict['external_evidence'], 1):
            result += f"{i}. {ev['title']} - {ev['link']}"
            result += f"Snippet: {ev['snippet']}\n"

        st.markdown(result)