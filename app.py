import streamlit as st
from src.rag import rag_chatbot

st.title("RAG Chatbot")

url = st.text_input("Enter URL")
question = st.text_input("Ask Question")

if st.button("Generate Answer"):

    answer = rag_chatbot(url, question)

    st.write("### Response:")
    st.success(answer)