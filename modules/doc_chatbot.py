import pytesseract
from PIL import Image
import PyPDF2
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# OCR for images and PDF parsing
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Chatbot that uses LangChain and text extraction
def doc_chatbot(uploaded_file):
    text = ""
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type in ["image/jpeg", "image/png"]:
        img = Image.open(uploaded_file)
        text = extract_text_from_image(img)

    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents([text], embeddings)
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="map_reduce", retriever=vector_store.as_retriever())

    query = "What is the warranty period?"
    response = qa.run(query)
    return response
