import gradio as gr
from src.rag import rag_chatbot

def chat(url, question):
    return rag_chatbot(url, question)

iface = gr.Interface(
    fn=chat,
    inputs=[
        gr.Textbox(label="Enter URL"),
        gr.Textbox(label="Ask Question")
    ],
    outputs="text",
    title="RAG Chatbot"
)

iface.launch()