from dotenv import load_dotenv
import os

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY")
)


messages = []

print("🤖 Welcome! Type 0 to exit")

while True:
    prompt = input("You: ")

    if prompt == "0":
        print("Goodbye")
        break

    
    messages.append(HumanMessage(content=prompt))

    
    response = model.invoke(messages)

    
    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)