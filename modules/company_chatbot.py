from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def company_chatbot(user_query):
    # Load company-specific knowledge base (add your docs here)
    company_docs = ["Document 1 text", "Document 2 text", "Company FAQ"]
    
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(company_docs, embeddings)
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="map_reduce", retriever=vector_store.as_retriever())

    response = qa.run(user_query)
    return response
