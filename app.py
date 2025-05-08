import streamlit as st
from modules.text_to_image import generate_image
from modules.text_to_video import generate_video
from modules.doc_chatbot import doc_chatbot
from modules.company_chatbot import company_chatbot

# Streamlit Layout
st.title("Multimodal AI App")
st.sidebar.title("Choose an option")

option = st.sidebar.selectbox(
    "Select Mode", 
    ("Text to Image", "Text to Video", "Document Chatbot", "Company Chatbot")
)

# Text-to-Image
if option == "Text to Image":
    st.header("Generate Image from Text")
    prompt = st.text_input("Enter a prompt:")
    if st.button("Generate Image"):
        img = generate_image(prompt)
        st.image(img)

# Text-to-Video
elif option == "Text to Video":
    st.header("Generate Video from Text")
    prompt = st.text_input("Enter a prompt:")
    if st.button("Generate Video"):
        video = generate_video(prompt)
        st.video(video)

# Document Chatbot
elif option == "Document Chatbot":
    st.header("Chat with Document")
    uploaded_file = st.file_uploader("Upload a Document", type=["pdf", "png", "jpeg"])
    if uploaded_file is not None:
        response = doc_chatbot(uploaded_file)
        st.write(response)

# Company Chatbot
elif option == "Company Chatbot":
    st.header("Chat with Company Bot")
    user_query = st.text_input("Ask the Company Bot a question:")
    if st.button("Ask"):
        response = company_chatbot(user_query)
        st.write(response)
