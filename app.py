import streamlit as st
from modules.text_to_image import generate_image
from modules.text_to_video import generate_video
from modules.doc_chatbot import doc_chatbot
from modules.company_chatbot import company_chatbot

# Set the title of the Streamlit app
st.title("Multimodal App")

# Define sidebar options
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose a feature:",
    ["Text to Image", "Text to Video", "Document Chatbot", "Company Chatbot"]
)

# Handle different features based on sidebar selection
if option == "Text to Image":
    st.header("Generate Image from Text")
    prompt = st.text_area("Enter a prompt for the image:")
    if st.button("Generate Image"):
        if prompt:
            image = generate_image(prompt)  # Function in your text_to_image.py module
            st.image(image, caption="Generated Image", use_column_width=True)
        else:
            st.error("Please enter a prompt to generate the image.")

elif option == "Text to Video":
    st.header("Generate Video from Text")
    prompt = st.text_area("Enter a prompt for the video:")
    if st.button("Generate Video"):
        if prompt:
            video = generate_video(prompt)  # Function in your text_to_video.py module
            st.video(video)  # Display the generated video
        else:
            st.error("Please enter a prompt to generate the video.")

elif option == "Document Chatbot":
    st.header("Chatbot for Documents")
    document = st.file_uploader("Upload a document", type=["pdf", "txt"])
    if document:
        response = doc_chatbot(document)  # Function in your doc_chatbot.py module
        st.write(response)

elif option == "Company Chatbot":
    st.header("Company-Specific Chatbot")
    user_input = st.text_input("Ask a question:")
    if user_input:
        response = company_chatbot(user_input)  # Function in your company_chatbot.py module
        st.write(response)
