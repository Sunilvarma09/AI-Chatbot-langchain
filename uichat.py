import streamlit as st
from dotenv import load_dotenv
import os

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Initialize model 
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY")
)

# UI Title
st.title("🤖 AI Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state.messages  

# Display previous messages
for msg in messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)


prompt = st.chat_input("You:")

if prompt:
    
    if prompt == "0":
        st.write("Goodbye 👋")
    else:
        messages.append(HumanMessage(content=prompt))

        response = model.invoke(messages)

        messages.append(AIMessage(content=response.content))
    

    st.chat_message("user").markdown(prompt)
    st.chat_message("assistant").markdown(response.content if prompt != "0" else "Goodbye 👋")