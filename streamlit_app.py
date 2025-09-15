import streamlit as st
from detectFakeNews import detect_fake_news
from PIL import Image

# Show title and description.
st.title("💬 No Fake News")

headline = st.text_input("Headline")
body = st.text_input("Body")

uploadedImage = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploadedImage is not None:
    # Display the uploaded image
    image = Image.open(uploadedImage)
    st.image(image, caption="Uploaded Image")

if st.button("Submit"):
    with st.spinner("Analyzing image and searching related news..."):
        verdict = detect_fake_news(headline = headline, body = body, uploadedImageFile = uploadedImage)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            result = verdict["gemini_verdict"]

            result += "\n=== Top Evidence Links ===\n"
            for i, ev in enumerate(verdict['external_evidence'], 1):
                result += f"{i}. {ev['title']} - {ev['link']}"
                result += f"Snippet: {ev['snippet']}\n"

            st.markdown(result)